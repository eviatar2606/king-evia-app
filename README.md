# king-evia-app

Progressive Web App (PWA) template for Eviatar's projects.

## Features
- ✅ Offline support with Service Worker
- ✅ Mobile-first design
- ✅ Installable on home screen
- ✅ Fast loading with caching
- ✅ Firebase Hosting deployment

## Getting Started

### Local Development
```bash
cd king-evia-app
# Serve locally (requires a simple HTTP server)
python -m http.server 8000
# or use: npx http-server
```

### Deployment
Push to `main` branch → GitHub Actions → Auto-deployed to Firebase! 🚀

## Project Structure
```
/
├── index.html       (Main application)
├── sw.js           (Service Worker for offline support)
├── manifest.json   (PWA configuration)
├── firebase.json   (Firebase hosting config)
└── .gitignore      (Git ignore rules)
```

## Live App
Visit: https://king-evia-app.web.app

---

Made with ❤️ by Eviatar
