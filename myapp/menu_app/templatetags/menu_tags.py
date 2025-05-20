from django import template
from ..models import MenuItem
from django.urls import resolve

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path
    menu_items = MenuItem.objects.filter(menu_name=menu_name).prefetch_related('children')
    menu_dict = {item.id: item for item in menu_items}

    def build_tree(item_id, parent_id=None):
        children = []
        for item in menu_items:
            if item.parent_id == item_id:
                children.append(build_tree(item.id, item.id))

        item_data = {
            'item': menu_dict.get(item_id),
            'children': children
        }
        return item_data

    root_items = [item for item in menu_items if item.parent_id is None]
    tree = [build_tree(item.id) for item in root_items]

    # Помечаем активные элементы
    def mark_active(node):
        node['item'].active = node['item'].is_active(current_path)
        for child in node['children']:
            mark_active(child)

    for node in tree:
        mark_active(node)


    # Развертываем меню
    def expand_parents(node):
        node['expanded'] = node['item'].active
        for child in node['children']:
            expand_parents(child)
            if child['expanded']:
                node['expanded'] = True

    for node in tree:
        expand_parents(node)

    return {'menu_items': tree}