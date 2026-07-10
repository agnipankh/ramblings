# Code Review

Review date: 2026-07-10

## Scope

This review covers the current uncommitted work:

- replacement of `content/technical/AssigningProbabilitiestoLLMOutputs.md` with `content/technical/AssigningProbabilitiestoLLMOutputs_v2.md`
- the new article images under `content/images/technical/`
- the MathJax additions in `themes/attila/templates/base.html`

The established two-repository Pelican and GitHub Pages publishing workflow described in `README.md` is treated as known-working.

## Findings

### High: MathJax configuration is declared after MathJax is loaded

`themes/attila/templates/base.html` loads the asynchronous MathJax script before assigning the global `MathJax` configuration object. If the remote script finishes first, it initializes with its defaults and the article's `$...$` inline delimiters may not be recognized. Define `window.MathJax` before the script tag that loads MathJax.

This should be addressed with a failing rendered-page test first. The test should exercise both inline `$...$` and display `$$...$$` delimiters through the generated public HTML.

### Resolved: The template loaded an unnecessary third-party polyfill

The page-wide third-party polyfill was removed from `themes/attila/templates/base.html`. The current MathJax v3 browser bundle does not require that dependency for supported browsers. A regression test now prevents the compromised domain from being reintroduced into the templates.

### Medium: The perplexity equation has an unmatched parenthesis

In `content/technical/AssigningProbabilitiestoLLMOutputs_v2.md`, the exponent is written as:

```text
2^{-\frac{1}{L_i} \sum_j \log(p_{ij}))}
```

There is one extra closing parenthesis after `\log(p_{ij})`. MathJax may render an error or misleading notation. The intended expression should be checked before editing the article.

### Medium: Related-article behavior has two implementations and misleading configuration

Both `content/extra/custom.js` and `content/extra/related-articles.js` implement the complete related-article feature, and both are loaded through `JS_OVERRIDE`. Registration order currently makes `custom.js` create the section while `related-articles.js` exits after detecting it. This works, but creates two sources of truth.

In addition, `MAX_RELATED_ARTICLES` and `SHOW_RELATED_ARTICLES` in `pelicanconf.py` do not control either browser implementation: the limit is hard-coded to `15`, and the scripts run whenever they are included. Consolidate the behavior behind one script and either wire the settings into generated markup or remove the settings. Start with browser-level behavior tests for exclusion of the current article and the maximum card count.

### Low: Feature documentation contradicts the current site structure

`README-branding-site.md` describes `content/pages/index.md` and `/blog.html`, but that page is absent and `pelicanconf.py` explicitly uses the normal blog index at `/`. The main `README.md` and `README-navigation.md` describe the current structure correctly. Mark the branding document as historical or update it to avoid misleading future maintenance.

### Low: One reference is not a Markdown list item

The Cunningham et al. sparse-autoencoder reference in the replacement article lacks the leading `*`. It will run into the preceding Yonatan reference instead of rendering as its own bibliography item.

## Verification

- Inspected the root configuration, publishing tasks, Makefile, feature documentation, theme templates, browser scripts, current Git diff, and theme submodule diff.
- After adding the uv-managed environment, `uv run make html` completed successfully and processed 17 articles and 1 page.
- No production code or article content was changed during this review.

## Recommended order

1. Add a rendered-page test for MathJax configuration order and equation delimiters, then fix the template.
2. Keep third-party browser dependencies minimal and covered by template tests.
3. Correct the perplexity expression and bibliography formatting.
4. Add browser-level tests, then consolidate the related-article implementation and configuration.
5. Reconcile the historical branding README with the current navigation docs.
