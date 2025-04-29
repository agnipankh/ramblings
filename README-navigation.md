# Navigation Menu Items

This document explains the navigation structure with "Blog", "Technical", "Business", and "Creative" links in the main menu.

## Configuration

1. **Menu Items Configuration**: The `pelicanconf.py` file contains:
   - Navigation menu items defined using the `MENUITEMS` parameter
   - Automatic category display disabled in the menu with `SHOW_CATEGORIES_ON_MENU = False`

```python
# Show categories in navigation menu
SHOW_CATEGORIES_ON_MENU = False  # We're using MENUITEMS instead for more control

# Menu items
MENUITEMS = (
    ('Blog', '/'),
    ('Technical', '/category/technical.html'),
    ('Business', '/category/business.html'),
    ('Creative', '/category/creative.html'),
)
```

## How It Works

The theme's navigation template (`/themes/attila/templates/partials/navigation-items.html`) automatically processes the `MENUITEMS` configuration to generate navigation links.

The navigation links will appear at the top of your site, allowing users to:
- Go to the Blog (main page)
- Browse posts filtered by the Technical category
- Browse posts filtered by the Business category
- Browse posts filtered by the Creative category

## Testing the Changes

After making these changes, you can test the navigation by regenerating your site:

```bash
# Clean the output directory
make clean

# Generate the site with your changes
make html

# Serve locally to test
make serve
```

Visit http://localhost:8000 in your browser. You should see the new navigation menu at the top of your site.

## Additional Customization (Optional)

If you want to modify the styling or behavior of the navigation menu, you can edit:
- `/themes/attila/templates/partials/navigation.html` - Overall navigation structure
- `/themes/attila/templates/partials/navigation-items.html` - Individual menu items
- `/themes/attila/static/css/style.css` - Navigation styling (look for `.nav-` classes)
