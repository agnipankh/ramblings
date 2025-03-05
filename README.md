
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

