## docker-jinja2
An image that renders an input string from env to a specified file.

## Environment Variables
All environment variables are avaliable under `env`
- `JINJA_INPUT_FILE`: The jinja2 template file path. ex: `/usr/src/app/template.j2`
- `JINJA_OUTPUT_FILE`: A file path where the output will be stored. ex: `/usr/src/app/tmp.sh`

## Examples

```bash
echo 'Hello {{ env.HOME }} {{ a }}' | jinjacli a=Bob > output.txt
```
