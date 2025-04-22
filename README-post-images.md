# Adding Post Images to the Main Page

This document outlines the changes needed to display post images on the main page of your blog.

## Changes Already Made

1. **Configuration Changes**: The `pelicanconf.py` file has been updated to:
   - Use the local theme path: `/Users/amit/Dropbox/DCode/ramblings/themes/attila`
   - Add configurations to show cover images: `SHOW_COVER_IN_LISTING = True` and `INDEX_COVER_IMAGE_HEIGHT = '250px'`

2. **Post Metadata**: Several posts have been updated to include a `Cover:` metadata field that points to the image to display:
   - `content/creative/Klimt_Kiss.md`
   - `content/creative/PlayingWithBokeh.md`
   - `content/creative/TheLittlePrince.md`
   - `content/technical/PlayingWithGamma.md`
   - `content/technical/NittyGrittyOfStyleTransfer.md`

## Changes Still Needed

1. **Template Modification**: You need to modify the theme's template file to display post cover images.
   - Edit: `/Users/amit/Dropbox/DCode/ramblings/themes/attila/templates/partials/loop.html`
   - Find the instructions in: `loop_html_changes.txt`

2. **CSS Styling**: Add the CSS styles for the post cover images.
   - Edit: `/Users/amit/Dropbox/DCode/ramblings/themes/attila/static/css/style.css`
   - Add the styles from: `post_image_styles.css`

## How to Apply the Changes

1. **Edit the Template File**:
   ```bash
   # Open the template file
   nano /Users/amit/Dropbox/DCode/ramblings/themes/attila/templates/partials/loop.html

   # Follow instructions in loop_html_changes.txt to add the code
   ```

2. **Add CSS Styles**:
   ```bash
   # Open the CSS file
   nano /Users/amit/Dropbox/DCode/ramblings/themes/attila/static/css/style.css

   # Append the contents of post_image_styles.css
   cat post_image_styles.css >> /Users/amit/Dropbox/DCode/ramblings/themes/attila/static/css/style.css
   ```

3. **Regenerate the Site**:
   ```bash
   # Clean the output directory
   make clean

   # Generate the site with your changes
   make html

   # Serve locally to test
   make serve
   ```

4. **Add Cover Images to More Posts** (Optional):
   - To add a cover image to any post, add the following line to the post's metadata section:
   ```
   Cover: /images/path/to/image.jpg
   ```

## Testing

After making these changes, you can test the site locally using:
```bash
make serve
```

This will serve the site at http://localhost:8000 where you can verify that post images are displayed on the main page.
