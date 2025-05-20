from django import template
from ..models import MenuItem
from django.urls import resolve

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    # Получаем все элементы меню с заданным именем
    menu_items = MenuItem.objects.filter(menu_name=menu_name).prefetch_related('children')

    # Создаем дерево
    root_items = [item for item in menu_items if item.parent is None]

    # Определяем активные элементы
    def mark_active(item):
        item.active = item.is_active(current_path)
        for child in item.children.all():
            mark_active(child)
        return item

    # Строим дерево с активными элементами
    def build_tree(items):
        result = []
        for item in items:
            marked_item = mark_active(item)
            children = build_tree(item.children.all())
            result.append({
                'item': marked_item,
                'children': children
            })
        return result

    tree = build_tree(root_items)

    # Разворачиваем родителей, если их дети активны
    def expand_parents(node):
        node['expanded'] = node['item'].active
        for child in node['children']:
            expand_parents(child)
            if child['expanded']:
                node['expanded'] = True
        return node

    expanded_tree = [expand_parents(item) for item in tree]

    return {
        'menu_items': expanded_tree
    }