## docker-jinja-reader
An image that renders an input string from env to a specified file.

## Environment Variables
All environment variables are avaliable under `env`
- `RENDER__INPUT`: The jinja2 template content. ex: `<body>{{ env.ENV_1 }}</body>`
- `RENDER__OUTPUT_FILE`: A file path where the output will be stored. ex: `/usr/src/app/tmp.sh`
