# Personal Portfolio Website

This is a personal portfolio website built using [Hugo](https://gohugo.io/), a fast and modern static site generator. The site features a clean, responsive design using a customized version of the hello-friend-ng theme.

## Features

- 🌍 Multi-language support (English and French)
- 💼 Portfolio/CV section
- 📝 Blog posts
- 🛠 Skills showcase with search functionality
- 🎨 Clean and modern design
- 🔄 Responsive layout

## Local Development

To run this site locally:

1. Install Hugo (extended version) on your machine
2. Clone this repository
3. Run the development server:

```bash
./start-dev.sh
```

Or manually with:

```bash
hugo server -D
```

The site will be available at `http://localhost:1313/`

## Building for Production

To build the site for production:

```bash
./start-prod.sh
```

Or manually with:

```bash
hugo --minify
```

The built site will be in the `public/` directory.

## Project Structure

- `content/` - All the content of the site (markdown files)
  - `posts/` - Blog posts
  - `about.md` - About page
  - `cv.md` - CV/Resume page
  - `skills.md` - Skills page
- `layouts/` - Custom layout templates
- `static/` - Static assets (images, icons, etc.)
- `themes/` - The hello-friend-ng-sab theme
- `hugo.toml` - Site configuration

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.