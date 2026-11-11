# ⚡ Modern Studio & Freelance Portfolio (Django)

A professional, full-stack Django website for a creative tech agency / freelance team specializing in **AI & Automation**, **Web Development**, **VR & 3D Environments**, and **Business Strategy**.

Includes an **advanced custom dark-themed admin dashboard** with **real-time page view analytics**, traffic charts, device breakdown, and an **inquiry management system**.

---

## 🌟 Key Features

### 🌐 Public Website
- **Modern Responsive Design**: Clean typography (Manrope font), smooth scrolling navigation, mobile-first responsive grid.
- **Service Offerings**: Showcases core disciplines (AI & Automation, Web Development, VR & 3D, Business Strategy).
- **Pricing Packages**: Transparent, tiered packages (Starter, Growth, Custom).
- **Portfolio & Case Studies**: Filterable project gallery with tags (VR/3D, AI/Data, Web, Strategy) and project links.
- **Team Section**: Dynamic member cards with role badges, bio, and LinkedIn integration.
- **Interactive FAQ**: Expandable accordion questions & answers.
- **Lead Capture & Contact Form**:
  - Honeypot anti-spam protection (`website` field filter).
  - Categorized inquiries with service and budget selector.
  - Automatic email notification dispatched to team inbox via Django `send_mail`.
  - Flash success messages on submission.

### 📊 Real-Time Analytics & Tracking
- **Built-in PageView Middleware**: Tracks every public request with zero external dependencies.
- **Device Detection**: Categorizes visits into Desktop, Mobile, and Tablet.
- **Privacy-Friendly**: Hashes visitor IP addresses using SHA-256 (no raw IPs stored).
- **Crawler & Static Filtering**: Automatically ignores admin routes, static/media assets, and known web bots/crawlers.

### 🎨 Custom Dark Admin Dashboard (`/admin/`)
- **Modern Purple & Dark UI**: High-contrast, sleek theme tailored for superusers.
- **Analytics Widgets**:
  - 👁 **Total Page Views**, **Views Today**, and **Last 7 Days**.
  - 📈 **7-Day Interactive Traffic Chart** powered by Chart.js.
  - 🔗 **Top Pages Ranking** with proportional visual progress bars.
  - 📱 **Device Split Breakdown** (Desktop / Mobile / Tablet).
- **Inquiry Management**:
  - Color-coded status badges (✓ Handled / ⏳ Pending).
  - Bulk actions: *Mark selected as handled* / *Mark selected as pending*.
  - Searchable by name, email, and message content; filterable by service and status.
  - One-click navigation to view and update leads directly from the dashboard.
- **Full Auth Management**: Includes Django User & Group management.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.13, Django 6.1
- **Database**: SQLite (default, easily switchable to PostgreSQL or MySQL)
- **Frontend**: HTML5, Vanilla CSS3 (Custom Responsive System), Chart.js
- **WSGI / Server**: Gunicorn, WhiteNoise (production static file serving)
- **Image Processing**: Pillow

---

## 📁 Project Structure

```text
Port/
├── .gitignore                   # Git ignore patterns (.env, pycache, etc.)
├── requirements.txt             # Python package dependencies
├── README.md                    # Project documentation
└── my_profile/                  # Django project root (manage.py location)
    ├── db.sqlite3               # SQLite database
    ├── manage.py                # Django CLI management script
    ├── my_profile/              # Project configuration
    │   ├── asgi.py
    │   ├── settings.py          # App settings, DB config, email settings
    │   ├── urls.py              # Root URL router
    │   └── wsgi.py
    ├── core/                    # Core application (home, inquiries, analytics)
    │   ├── admin.py             # Custom AdminSite & Inquiry / PageView admins
    │   ├── middleware.py        # Real-time PageView tracking middleware
    │   ├── models.py            # Inquiry & PageView database models
    │   ├── forms.py             # InquiryForm with honeypot validation
    │   ├── views.py             # Home view & contact form handler
    │   └── management/
    │       └── commands/
    │           └── seed.py      # Starter data seeder for team & projects
    ├── projects/                # Projects & case studies app
    │   ├── models.py            # Project model (category, year, image, URL)
    │   ├── views.py             # Project listing & category filtering
    │   └── admin.py             # Project admin configuration
    ├── team/                    # Team members app
    │   ├── models.py            # TeamMember model (name, role, bio, order)
    │   └── admin.py             # Team member ordering & admin
    ├── templates/               # HTML templates
    │   ├── base.html            # Base layout & navigation
    │   ├── admin/
    │   │   ├── base_site.html   # Custom dark admin theme & styling
    │   │   └── index.html       # Analytics dashboard & stat widgets
    │   ├── core/
    │   │   └── home.html        # Main landing page
    │   └── projects/
    │       ├── list.html        # All projects view
    │       └── _card.html       # Reusable project card partial
    └── static/                  # Static assets
        └── css/
            └── style.css        # Public website styles
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.11+ (Python 3.13 recommended)
- `pip` and `virtualenv`

### 2. Set Up Virtual Environment

```bash
# Clone or navigate to the repository directory
cd d:\ai\Port

# Activate the existing virtual environment (.env)
# On Windows (PowerShell):
.env\Scripts\Activate.ps1

# Or on Windows (Command Prompt):
.env\Scripts\activate.bat

# Or on Linux / macOS:
source .env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (`.env`)

Create or update a `.env` file in `d:\ai\Port\` or set environment variables:

```ini
DEBUG=True
CONTACT_EMAIL=your-email@example.com
DEFAULT_FROM_EMAIL=your-email@example.com

# For development (prints emails to the terminal console):
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Or for production with Gmail SMTP:
# EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
# EMAIL_HOST_USER=your-email@gmail.com
# EMAIL_HOST_PASSWORD=your-app-password
```

### 5. Apply Migrations

```bash
cd my_profile
python manage.py migrate
```

### 6. Seed Initial Data (Optional)

Populate default team members and initial portfolio projects with the built-in seed command:

```bash
python manage.py seed
```

### 7. Create a Superuser

To log into the custom admin dashboard, create an administrator account:

```bash
python manage.py createsuperuser
```
Follow the prompts to enter your username, email, and password.

### 8. Run Development Server

```bash
python manage.py runserver
```

Open your browser:
- **Public Site**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Dashboard**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## ☁️ Deployment on Render (Step-by-Step)

1. Connect your GitHub repository to a new **Web Service** on Render.
2. In service settings:
   - **Root Directory**: `my_profile`
   - **Build Command**: `pip install -r ../requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input`
   - **Start Command**: `gunicorn my_profile.wsgi:application`
3. In **Environment Variables**:
   - `DEBUG` = `FALSE`
   - `SECRET_KEY` = `<your-secret-key>`
   - `ALLOWED_HOSTS` = `.onrender.com`
4. Deploy! Your site and custom admin panel will go live in 2-3 minutes.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
