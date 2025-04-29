# Related Articles Feature

This document explains the implementation of the related articles feature, which displays thumbnails of related content at the bottom of each article page.

## Overview

The related articles feature enhances navigation by showing readers additional content from the same category. This encourages exploration and increases engagement with the website's content.

## Implementation Details

The feature is implemented through two main files:

1. **Custom CSS** (`content/extra/custom.css`)
   - Provides styling for the related articles grid
   - Defines card animations and hover effects
   - Includes responsive design for different screen sizes

2. **JavaScript** (`content/extra/related-articles.js`)
   - Dynamically creates the related articles section on article pages
   - Fetches articles from the same category as the current article
   - Randomly selects up to 15 articles to display
   - Creates card elements with images and titles

### How It Works

1. The JavaScript code executes when a page loads, detecting if the current page is an article
2. It determines the current article's category from the page metadata
3. It creates a "Related Articles" section and inserts it after the post navigation element
4. It fetches the category page to get all articles in that category
5. It filters out the current article and randomly selects up to 15 other articles
6. It creates card elements for each selected article, including:
   - A thumbnail image (from the article's cover image when available)
   - The article title
   - A link to the article
7. The cards are displayed in a responsive grid layout at the bottom of the article

## Configuration

The feature is configured in `pelicanconf.py`:

```python
# Static paths for CSS and JS files
STATIC_PATHS = ['images', 'extra/CNAME', 'extra/custom.css', 'extra/related-articles.js', ...]
EXTRA_PATH_METADATA = {
    # Other mappings...
    'extra/custom.css': {'path': 'theme/css/custom.css'},
    'extra/related-articles.js': {'path': 'theme/js/related-articles.js'},
}

# Include custom CSS and JS files in the theme
CSS_OVERRIDE = ['theme/css/custom.css']
JS_OVERRIDE = ['theme/js/custom.js', 'theme/js/related-articles.js']

# Related articles settings
SHOW_RELATED_ARTICLES = True
MAX_RELATED_ARTICLES = 15
```

## Customization

### Changing the Number of Related Articles

To change the maximum number of related articles displayed, modify both:

1. The `MAX_RELATED_ARTICLES` setting in `pelicanconf.py`
2. The `slice(0, 15)` line in `related-articles.js`

### Styling Changes

The appearance of the related articles section can be customized by modifying the CSS in `custom.css`. Key styling classes include:

- `.related-articles` - The container for the entire section
- `.related-articles-title` - The section title
- `.related-articles-grid` - The grid layout for the cards
- `.related-article-card` - Individual article cards
- `.related-article-image` - Image container within each card
- `.related-article-title` - Title text within each card

### Example: Changing Card Appearance

To change the appearance of the article cards, modify the CSS like this:

```css
.related-article-card {
  border-radius: 4px; /* Less rounded corners */
  box-shadow: 0 2px 5px rgba(0,0,0,0.2); /* Stronger shadow */
  background: #f9f9f9; /* Light gray background */
}

.related-article-title {
  font-size: 0.9rem; /* Smaller text */
  font-weight: 700; /* Bolder text */
  color: #222; /* Darker text color */
}
```

## Testing

After making changes to the CSS or JavaScript, rebuild the site to see your changes:

```bash
$ pelican content -o output -s pelicanconf.py
$ pelican --listen
```

Visit an article page to verify that the related articles section appears correctly.

## Troubleshooting

If the related articles section doesn't appear:

1. Check the browser console for JavaScript errors
2. Verify that the JavaScript files are being loaded (check Network tab in developer tools)
3. Ensure the article has a category assigned
4. Confirm there are other articles in the same category
5. Check your DOM selectors - the script needs to find elements with the correct class names

## Future Enhancements

Potential improvements to consider:

1. Add filtering options (e.g., by tag or date)
2. Implement true "related" functionality based on content similarity rather than just category
3. Add view counts to highlight popular articles
4. Implement lazy loading for images to improve performance
5. Add caching mechanism to avoid fetching the category page on every page load
