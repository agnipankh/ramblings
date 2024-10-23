
## How To

 [Github Pelican Docs](https://docs.getpelican.com/en/latest/tips.html#publishing-to-github-pages-using-a-custom-github-actions-workflow)

## Creating Content

Once content is created run the following to see the content locally. The content should live inside the "$/content" directory

```
$ pelican content -o output -s pelicanconf.py
$ ghp-import output -b gh-pages
$ pelican --listen
```

## 

```



$ git push git@github.com:agnipankh/agnipankh.github.io.git gh-pages:main
## The above only establishes a transient connection to the remote repo
```


