# menu_items_test

Django app implementing a tree-like menu:

Requirements:

1) Menu via Template Tag: The menu rendering should be encapsulated within a Django template tag for easy inclusion in templates.
2) Dynamic Expansion: All parent items (ancestors) of the currently active menu item should be expanded/visible.
The first level of children directly under the active menu item should also be expanded.
3) Database Storage: Menu structure and data should be stored in the Django database.
4) Admin Interface: The menu should be manageable through Django’s standard admin interface.
5) Active Item Determination: The currently active menu item is determined by matching the menu item’s URL to the current page’s URL.
6) Multiple Menus: The application must support multiple menus on a single page. These menus are distinguished by name.
7) URL Handling: Clicking a menu item navigates to the associated URL. URLs can be specified either explicitly or using Django’s named URL patterns.
8) Single Database Query: Each menu rendering should require only one database query to retrieve all necessary menu data.
