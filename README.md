
## How To

There are two repos for this. Ramblings which serves as the content manager and agnipankh.github.io that serves as the HTML site. We use pelican to do this. The various variables are set in pelicanconf.py

You will always work in the main branch of Rambling.

 [Github Pelican Docs](https://docs.getpelican.com/en/latest/tips.html#publishing-to-github-pages-using-a-custom-github-actions-workflow)

## Creating Content

Once content is created run the following to see the content locally. The content should live inside the "$/content" directory

```
$ pelican content -o output -s pelicanconf.py
$ ghp-import output -b gh-pages
$ pelican --listen
```

## Pushing Content to the live site


```
$ git push git@github.com:agnipankh/agnipankh.github.io.git gh-pages:main
## The above only establishes a transient connection to the remote repo
```

## Committing content to the CMS

When you are done making any changes to the content. Just `git add` and `git commit` like normal and push the code to the repo.

## Site Structure

The site uses a simplified structure with the following pages:
- Blog (main landing page)
- Technical (category page)
- Business (category page)
- Creative (category page)
- About (page)

See [README-navigation.md](README-navigation.md) for details on the navigation menu structure.

## Related Articles Feature

Individual article pages display related content thumbnails at the bottom. This feature:

1. Shows thumbnails of random articles from the same category
2. Limits the display to a maximum of 15 thumbnails
3. Makes each thumbnail clickable, linking to the respective article
4. Uses article cover images when available

The related articles feature is implemented using custom CSS and JavaScript:
- `content/extra/custom.css` - Styling for the related articles grid
- `content/extra/custom.js` - JavaScript to dynamically populate related articles
