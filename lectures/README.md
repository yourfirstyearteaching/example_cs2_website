This directory will be statically served by Apache, not flask. So, it needs a `.htaccess` file that has the following line:

```
RewriteEngine Off
```

