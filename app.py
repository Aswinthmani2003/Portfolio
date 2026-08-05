from flask import Flask, render_template_string

app = Flask(__name__)

# HTML Template with Navigation and Individual Project Pages
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aswinthmani V - Portfolio</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f7fa;
        }
        
        /* Navigation Bar */
        nav {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 0;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        .nav-container {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
        }
        
        .logo {
            color: white;
            font-size: 1.5em;
            font-weight: bold;
            padding: 20px 0;
        }
        
        .nav-links {
            display: flex;
            list-style: none;
            gap: 0;
        }
        
        .nav-links li {
            position: relative;
        }
        
        .nav-links li a {
            color: white;
            text-decoration: none;
            padding: 25px 20px;
            display: block;
            transition: all 0.3s;
            border-bottom: 3px solid transparent;
        }
        
        .nav-links li a:hover,
        .nav-links li a.active {
            background: rgba(255, 255, 255, 0.1);
            border-bottom: 3px solid white;
        }
        
        /* Dropdown Menu */
        .dropdown {
            position: relative;
        }
        
        .dropdown-content {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-width: 320px;

    max-height: 70vh;          /* KEY FIX */
    overflow-y: auto;          /* KEY FIX */

    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    z-index: 2000;
}

        
        .dropdown:hover .dropdown-content {
            display: block;
        }
        
        .dropdown-content a {
            color: white;
            padding: 15px 20px;
            text-decoration: none;
            display: block;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s;
        }
        
        .dropdown-content a:hover {
            background: rgba(255, 255, 255, 0.15);
            padding-left: 30px;
        }
        
        .mobile-menu-toggle {
            display: none;
            background: none;
            border: none;
            color: white;
            font-size: 1.5em;
            cursor: pointer;
            padding: 10px;
        }
        
        /* Container */
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        
        /* Tab Content */
        .tab-content {
            display: none;
            animation: fadeIn 0.5s;
        }
        
        .tab-content.active {
            display: block;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Hero Section */
        .hero {
            background: white;
            padding: 60px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-bottom: 40px;
        }
        
        .hero h1 {
            color: #667eea;
            font-size: 3em;
            margin-bottom: 15px;
        }
        
        .hero .title {
            color: #764ba2;
            font-size: 1.5em;
            margin-bottom: 20px;
        }
        
        .hero .tagline {
            color: #666;
            font-size: 1.1em;
            max-width: 800px;
            margin: 0 auto 30px;
        }
        
        .contact-links {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 30px;
        }
        
        .contact-btn {
            color: white;
            text-decoration: none;
            padding: 12px 25px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 25px;
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        
        .contact-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .cert-btn {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            margin-top: 14px;
            padding: 7px 16px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 20px;
            font-size: 13px;
            transition: all 0.3s;
        }

        .cert-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }

        /* Section Styling */
        .section {
            background: white;
            padding: 40px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
        }
        
        .section h2 {
            color: #667eea;
            margin-bottom: 30px;
            font-size: 2.2em;
            position: relative;
            padding-bottom: 15px;
        }
        
        .section h2:after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 60px;
            height: 4px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 2px;
        }
        
        /* Project Detail Page */
        .project-detail-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 50px;
            border-radius: 15px;
            margin-bottom: 30px;
        }
        
        .project-detail-header h1 {
            font-size: 2.5em;
            margin-bottom: 15px;
        }
        
        .project-meta {
            display: flex;
            gap: 30px;
            flex-wrap: wrap;
            margin-top: 20px;
            font-size: 1.1em;
        }
        
        .project-meta-item {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .project-overview {
            background: white;
            padding: 40px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
        }
        
        .project-overview h2 {
            color: #667eea;
            margin-bottom: 20px;
            font-size: 2em;
        }
        
        .project-overview p {
            font-size: 1.1em;
            line-height: 1.8;
            color: #555;
            margin-bottom: 15px;
        }
        
        .tech-stack-detail {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 25px;
        }
        
        .tech-badge-large {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 1em;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-top: 25px;
        }
        
        .feature-card {
            background: #f8f9fa;
            padding: 25px;
            border-radius: 12px;
            border-left: 4px solid #667eea;
        }
        
        .feature-card h3 {
            color: #764ba2;
            margin-bottom: 10px;
            font-size: 1.2em;
        }
        
        .feature-card p {
            color: #555;
            line-height: 1.6;
        }
        
        .screenshots-section {
            background: white;
            padding: 40px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
        }
        
        .screenshots-section h2 {
            color: #667eea;
            margin-bottom: 30px;
            font-size: 2em;
        }
        
        .screenshots-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 30px;
        }
        
        .screenshot-item {
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .profile-photo {
    width: 140px;              /* control size */
    height: 140px;

    border-radius: 50%;        /* makes it round */
    object-fit: cover;         /* crops properly */

    display: block;
    margin: 0 auto 18px auto;  /* center + spacing */

    border: 3px solid rgba(118, 75, 162, 0.5);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
}

        
        .screenshot-placeholder {
            background: linear-gradient(135deg, #e8eaf6 0%, #f3e5f5 100%);
            border: 2px dashed #9fa8da;
            border-radius: 10px;
            padding: 80px 40px;
            text-align: center;
            color: #5c6bc0;
            min-height: 300px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-style: italic;
        }
        
        .screenshot-placeholder:before {
            content: '📸';
            font-size: 4em;
            margin-bottom: 15px;
        }
        
        .screenshot-caption {
            background: #f8f9fa;
            padding: 15px;
            text-align: center;
            color: #555;
            font-weight: 500;
        }
        
        /* Back Button */
        .back-button {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            color: white;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 12px 25px;
            border-radius: 25px;
            text-decoration: none;
            margin-bottom: 30px;
            transition: all 0.3s;
        }
        
        .back-button:hover {
            transform: translateX(-5px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        /* About Section */
        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            align-items: start;
        }
        
        .about-text p {
            margin-bottom: 15px;
            line-height: 1.8;
            color: #555;
        }
        
        .about-highlights {
            background: #f8f9fa;
            padding: 30px;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }
        
        .about-highlights h3 {
            color: #764ba2;
            margin-bottom: 15px;
        }
        
        .about-highlights ul {
            list-style: none;
        }
        
        .about-highlights li {
            padding: 8px 0;
            color: #555;
            position: relative;
            padding-left: 25px;
        }
        
        .about-highlights li:before {
            content: '✓';
            position: absolute;
            left: 0;
            color: #667eea;
            font-weight: bold;
        }
        
        /* Education */
        .education-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px;
            border-radius: 15px;
            color: white;
        }
        
        .education-card h3 {
            font-size: 1.8em;
            margin-bottom: 10px;
        }
        
        .education-card .degree {
            font-size: 1.2em;
            margin-bottom: 20px;
            opacity: 0.95;
        }
        
        .education-details {
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            margin-top: 20px;
        }
        
        .education-detail-item {
            flex: 1;
            min-width: 200px;
        }
        
        .education-detail-item strong {
            display: block;
            font-size: 0.9em;
            opacity: 0.8;
            margin-bottom: 5px;
        }
        
        /* Skills Grid */
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }
        
        .skill-card {
            background: #f8f9fa;
            padding: 30px;
            border-radius: 12px;
            transition: all 0.3s;
            border-top: 4px solid #667eea;
        }
        
        .skill-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }
        
        .skill-card h3 {
            color: #764ba2;
            margin-bottom: 20px;
            font-size: 1.3em;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .skill-card ul {
            list-style: none;
        }
        
        .skill-card li {
            padding: 8px 0;
            color: #555;
            position: relative;
            padding-left: 20px;
        }
        
        .skill-card li:before {
            content: '▪';
            position: absolute;
            left: 0;
            color: #667eea;
        }
        
        /* Projects Overview */
        .project-card {
            background: white;
            padding: 35px;
            border-radius: 12px;
            margin-bottom: 30px;
            border: 1px solid #e0e0e0;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }
        
        .project-card:before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 5px;
            height: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        .project-card:hover {
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
            transform: translateY(-3px);
        }
        
        .project-header {
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 20px;
            flex-wrap: wrap;
            gap: 10px;
        }
        
        .project-card h3 {
            color: #667eea;
            font-size: 1.6em;
            margin: 0;
        }
        
        .project-date {
            color: #999;
            font-size: 0.95em;
            padding: 5px 15px;
            background: #f0f0f0;
            border-radius: 20px;
        }
        
        .project-card p {
            color: #555;
            line-height: 1.6;
            margin-bottom: 15px;
        }
        
        .view-details-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: white;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 10px 20px;
            border-radius: 20px;
            text-decoration: none;
            margin-top: 15px;
            transition: all 0.3s;
        }
        
        .view-details-btn:hover {
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        /* Interests */
        .interests-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        
        .interest-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 12px;
            text-align: center;
            transition: all 0.3s;
        }
        
        .interest-card:hover {
            transform: scale(1.05);
        }
        
        .interest-card .icon {
            font-size: 3em;
            margin-bottom: 15px;
        }
        
        .interest-card h3 {
            font-size: 1.2em;
        }
        
        /* Contact Page */
        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 30px;
        }
        
        .contact-card {
            background: #f8f9fa;
            padding: 40px;
            border-radius: 12px;
            text-align: center;
            transition: all 0.3s;
            border-top: 4px solid #667eea;
        }
        
        .contact-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }
        
        .contact-card .icon {
            font-size: 3em;
            margin-bottom: 20px;
        }
        
        .contact-card h3 {
            color: #764ba2;
            margin-bottom: 15px;
            font-size: 1.3em;
        }
        
        .contact-card p {
            color: #555;
            word-break: break-all;
        }
        
        .contact-card a {
            color: #667eea;
            text-decoration: none;
        }
        
        .contact-card a:hover {
            text-decoration: underline;
        }
        
        /* Footer */
        footer {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            padding: 30px 20px;
            margin-top: 60px;
        }
        
        /* Responsive Design */
        @media (max-width: 968px) {
            .mobile-menu-toggle {
                display: block;
            }
            
            .nav-links {
                display: none;
                position: absolute;
                top: 100%;
                left: 0;
                right: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                flex-direction: column;
                box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
            }
            
            .nav-links.active {
                display: flex;
            }
            
            .nav-links li a {
                padding: 20px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            }
            
            .dropdown-content {
                position: static;
                display: none;
                box-shadow: none;
            }
            
            .dropdown.active .dropdown-content {
                display: block;
            }
            
            .hero h1 {
                font-size: 2em;
            }
            
            .hero {
                padding: 40px 20px;
            }
            
            .about-content {
                grid-template-columns: 1fr;
            }
            
            .skills-grid,
            .interests-grid,
            .contact-grid,
            .screenshots-grid {
                grid-template-columns: 1fr;
            }
            
            .section {
                padding: 25px;
            }
            
            .project-detail-header {
                padding: 30px 20px;
            }
            
            .project-detail-header h1 {
                font-size: 1.8em;
            }
        }
    </style>

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

    <!-- Flag JS early so reveal states never trap content for no-JS users -->
    <script>document.documentElement.className += ' js';</script>

    <!-- ============================================================
         DARK / NEON LAYER — overrides the base sheet above
         ============================================================ -->
    <style>
    :root {
        --bg:        #07070c;
        --glass:     rgba(255,255,255,.035);
        --glass-2:   rgba(255,255,255,.06);
        --stroke:    rgba(255,255,255,.08);
        --stroke-2:  rgba(255,255,255,.16);
        --neon:      #8b7cff;
        --neon-2:    #c86bff;
        --cyan:      #22d3ee;
        --txt:       #ececf5;
        --txt-2:     #9b9bb0;
        --txt-3:     #70708a;
        --grad:      linear-gradient(120deg,#8b7cff 0%,#c86bff 50%,#22d3ee 100%);
        --radius:    18px;
    }

    /* ---------- Base ---------- */
    html { scroll-behavior: smooth; }

    body {
        background: var(--bg) !important;
        color: var(--txt) !important;
        font-family: 'Inter', system-ui, sans-serif !important;
        overflow-x: hidden;
        -webkit-font-smoothing: antialiased;
    }

    h1,h2,h3,.logo { font-family:'Space Grotesk', system-ui, sans-serif !important; letter-spacing:-.02em; }

    ::selection { background: rgba(139,124,255,.35); color:#fff; }

    /* ---------- Custom scrollbar ---------- */
    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: #0a0a12; }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg,var(--neon),var(--neon-2));
        border-radius: 10px;
        border: 2px solid #0a0a12;
    }
    ::-webkit-scrollbar-thumb:hover { background: linear-gradient(180deg,var(--neon-2),var(--cyan)); }

    /* ---------- Animated background mesh ---------- */
    .bg-mesh {
        position: fixed; inset: 0;
        z-index: 0; pointer-events: none; overflow: hidden;
    }
    .bg-mesh .blob {
        position: absolute; border-radius: 50%;
        filter: blur(90px); opacity: .5;
        will-change: transform;
    }
    .bg-mesh .b1 {
        width: 46vw; height: 46vw; top: -12vw; left: -10vw;
        background: radial-gradient(circle,#5b3cff 0%,transparent 70%);
        animation: drift1 24s ease-in-out infinite;
    }
    .bg-mesh .b2 {
        width: 40vw; height: 40vw; top: 30vh; right: -14vw;
        background: radial-gradient(circle,#c439ff 0%,transparent 70%);
        animation: drift2 30s ease-in-out infinite;
    }
    .bg-mesh .b3 {
        width: 34vw; height: 34vw; bottom: -10vw; left: 25vw;
        background: radial-gradient(circle,#0891b2 0%,transparent 70%);
        animation: drift3 27s ease-in-out infinite;
    }
    @keyframes drift1 {
        0%,100% { transform: translate(0,0) scale(1); }
        33%     { transform: translate(8vw,10vh) scale(1.15); }
        66%     { transform: translate(-4vw,6vh) scale(.9); }
    }
    @keyframes drift2 {
        0%,100% { transform: translate(0,0) scale(1); }
        50%     { transform: translate(-12vw,-8vh) scale(1.2); }
    }
    @keyframes drift3 {
        0%,100% { transform: translate(0,0) scale(1); }
        40%     { transform: translate(10vw,-12vh) scale(1.1); }
        75%     { transform: translate(-6vw,4vh) scale(.95); }
    }
    /* faint tech grid on top of the blobs */
    .grid-overlay {
        position: absolute; inset: 0;
        background-image:
            linear-gradient(rgba(255,255,255,.028) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,.028) 1px, transparent 1px);
        background-size: 54px 54px;
        mask-image: radial-gradient(ellipse 90% 60% at 50% 0%, #000 25%, transparent 78%);
        -webkit-mask-image: radial-gradient(ellipse 90% 60% at 50% 0%, #000 25%, transparent 78%);
    }

    /* Keep nav above page content — it owns its own stacking context, so the
       dropdown's z-index only competes inside it, not against .container. */
    .container, footer { position: relative; z-index: 2; }
    nav { position: sticky; top: 0; z-index: 1000; }

    /* ---------- Scroll progress bar ---------- */
    .scroll-progress {
        position: fixed; top: 0; left: 0; height: 3px; width: 0%;
        background: var(--grad);
        z-index: 5000;
        box-shadow: 0 0 14px rgba(139,124,255,.9);
        transition: width .08s linear;
    }

    /* ---------- Cursor glow ---------- */
    .cursor-glow {
        position: fixed; top: 0; left: 0;
        width: 420px; height: 420px; border-radius: 50%;
        pointer-events: none; z-index: 1;
        background: radial-gradient(circle, rgba(139,124,255,.13) 0%, transparent 62%);
        transform: translate(-50%,-50%);
        opacity: 0; transition: opacity .4s ease;
    }
    @media (hover:hover) and (min-width: 969px) { .cursor-glow.on { opacity: 1; } }

    /* ---------- Nav ---------- */
    nav {
        background: rgba(9,9,16,.72) !important;
        backdrop-filter: blur(20px) saturate(160%);
        -webkit-backdrop-filter: blur(20px) saturate(160%);
        border-bottom: 1px solid var(--stroke);
        box-shadow: 0 4px 30px rgba(0,0,0,.5) !important;
    }
    .logo {
        background: var(--grad);
        -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 200% auto;
        animation: shimmer 6s linear infinite;
        font-weight: 700 !important;
    }
    @keyframes shimmer { to { background-position: 200% center; } }

    .nav-links li a { color: var(--txt-2) !important; font-size:.95em; font-weight:500; border-bottom:none !important; position:relative; }
    .nav-links li a::after {
        content:''; position:absolute; left:20px; right:20px; bottom:16px; height:2px;
        background: var(--grad); border-radius:2px;
        transform: scaleX(0); transform-origin:left; transition: transform .32s cubic-bezier(.4,0,.2,1);
    }
    .nav-links li a:hover { background: transparent !important; color: var(--txt) !important; }
    .nav-links li a:hover::after { transform: scaleX(1); }
    .nav-links li a.active {
        background: transparent !important; color: #fff !important;
        text-shadow: 0 0 18px rgba(139,124,255,.65);
    }
    .nav-links li a.active::after { transform: scaleX(1); }

    .dropdown-content {
        background: rgba(11,11,20,.94) !important;
        backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
        border: 1px solid var(--stroke);
        border-radius: 14px; margin-top: 6px; padding: 6px;
        box-shadow: 0 24px 60px rgba(0,0,0,.7), 0 0 0 1px rgba(139,124,255,.1) !important;
    }
    .dropdown-content a {
        color: var(--txt-2) !important; border-bottom: none !important;
        border-radius: 9px; font-size: .9em; padding: 12px 16px !important;
    }
    .dropdown-content a:hover {
        background: rgba(139,124,255,.14) !important;
        color: #fff !important; padding-left: 22px !important;
    }
    .mobile-menu-toggle { color: var(--txt) !important; }

    /* ---------- Glass surfaces ---------- */
    .hero, .section, .project-overview, .screenshots-section {
        background: var(--glass) !important;
        backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
        border: 1px solid var(--stroke);
        border-radius: var(--radius) !important;
        box-shadow: 0 20px 60px rgba(0,0,0,.42) !important;
    }

    /* ---------- Hero ---------- */
    .hero { position: relative; overflow: hidden; padding: 70px 50px !important; }
    .hero::before {
        content:''; position:absolute; top:-1px; left:12%; right:12%; height:1px;
        background: linear-gradient(90deg,transparent,var(--neon),var(--cyan),transparent);
    }
    .hero h1 {
        font-size: clamp(2.3em, 6vw, 4em) !important;
        background: var(--grad);
        -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 220% auto;
        animation: shimmer 7s linear infinite;
        font-weight: 700; margin-bottom: 18px !important;
    }
    .hero h1 .caret {
        -webkit-text-fill-color: var(--cyan); color: var(--cyan);
        font-weight: 300; animation: blink 1s step-end infinite;
    }
    @keyframes blink { 50% { opacity: 0; } }

    .hero .title { color: var(--txt) !important; font-weight: 500; opacity: .92; }
    .hero .tagline { color: var(--txt-2) !important; }

    .profile-photo {
        border: 1px solid var(--stroke-2) !important;
        box-shadow: 0 0 0 6px rgba(139,124,255,.07), 0 0 50px rgba(139,124,255,.35) !important;
        transition: transform .5s cubic-bezier(.34,1.56,.64,1), box-shadow .5s ease;
    }
    .profile-photo:hover {
        transform: scale(1.07) rotate(2.5deg);
        box-shadow: 0 0 0 8px rgba(139,124,255,.12), 0 0 70px rgba(200,107,255,.55) !important;
    }

    /* ---------- Headings ---------- */
    .section h2, .project-overview h2, .screenshots-section h2 {
        color: var(--txt) !important;
        font-size: 2em !important; font-weight: 600;
    }
    .section h2:after {
        background: var(--grad) !important;
        width: 54px !important; height: 3px !important;
        box-shadow: 0 0 16px rgba(139,124,255,.8);
    }

    /* gradient text for the inline-styled purple sub-headings */
    h3[style*="#764ba2"] {
        background: var(--grad);
        -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 600;
    }

    /* ---------- Buttons ---------- */
    .contact-btn, .cert-btn, .view-details-btn, .back-button {
        background: rgba(139,124,255,.1) !important;
        border: 1px solid rgba(139,124,255,.3);
        color: var(--txt) !important;
        position: relative; overflow: hidden;
        transition: transform .3s cubic-bezier(.34,1.4,.64,1), box-shadow .3s, border-color .3s, background .3s;
    }
    .contact-btn::before, .cert-btn::before, .view-details-btn::before, .back-button::before {
        content:''; position:absolute; inset:0;
        background: var(--grad); opacity:0; transition: opacity .3s;
        z-index:-1;
    }
    .contact-btn:hover, .cert-btn:hover, .view-details-btn:hover, .back-button:hover {
        background: rgba(139,124,255,.2) !important;
        border-color: rgba(200,107,255,.65);
        color: #fff !important;
        box-shadow: 0 10px 34px rgba(139,124,255,.35), 0 0 0 1px rgba(200,107,255,.25) !important;
        transform: translateY(-3px) !important;
    }
    .back-button:hover { transform: translateX(-6px) !important; }
    .view-details-btn:hover { transform: translateX(6px) !important; }

    /* ---------- Cards (glass + mouse spotlight) ---------- */
    .skill-card, .feature-card, .contact-card, .project-card,
    .about-highlights, .interest-card, .education-card {
        background: var(--glass) !important;
        backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--stroke) !important;
        border-radius: 16px !important;
        position: relative; overflow: hidden;
        transition: transform .4s cubic-bezier(.34,1.3,.64,1), border-color .4s, box-shadow .4s, background .4s;
    }
    /* radial spotlight that tracks the pointer */
    .skill-card::after, .feature-card::after, .contact-card::after,
    .project-card::after, .interest-card::after {
        content:''; position:absolute; inset:0; pointer-events:none;
        background: radial-gradient(340px circle at var(--mx,50%) var(--my,50%), rgba(139,124,255,.14), transparent 60%);
        opacity: 0; transition: opacity .35s;
    }
    .skill-card:hover::after, .feature-card:hover::after, .contact-card:hover::after,
    .project-card:hover::after, .interest-card:hover::after { opacity: 1; }

    .skill-card:hover, .feature-card:hover, .contact-card:hover, .interest-card:hover {
        transform: translateY(-7px) !important;
        border-color: var(--stroke-2) !important;
        box-shadow: 0 22px 55px rgba(0,0,0,.55), 0 0 0 1px rgba(139,124,255,.2) !important;
    }

    .skill-card  { border-top: 1px solid var(--stroke) !important; }
    .contact-card{ border-top: 1px solid var(--stroke) !important; }
    .skill-card::before, .contact-card::before {
        content:''; position:absolute; top:0; left:0; right:0; height:2px;
        background: var(--grad); opacity:.85;
    }
    /* Neon left rail via pseudo-element — a translucent fill layer let the
       gradient bleed through the whole card, so use a real overlay instead. */
    .feature-card, .about-highlights {
        border-left: 1px solid var(--stroke) !important;
        background: var(--glass) !important;
    }
    .feature-card::before, .about-highlights::before {
        content: ''; position: absolute;
        left: 0; top: 0; bottom: 0; width: 2px;
        background: var(--grad);
        box-shadow: 0 0 18px rgba(139,124,255,.55);
    }

    .skill-card h3, .feature-card h3, .contact-card h3, .about-highlights h3 {
        color: var(--txt) !important; font-weight: 600;
    }
    .skill-card li:before { color: var(--neon) !important; }
    .about-highlights li:before { color: var(--cyan) !important; }
    .skill-card li, .about-highlights li, .feature-card p,
    .contact-card p, .about-text p, .project-overview p {
        color: var(--txt-2) !important;
    }

    /* ---------- Interest / education cards ---------- */
    .interest-card, .education-card {
        background: linear-gradient(140deg, rgba(139,124,255,.13), rgba(200,107,255,.07)) !important;
    }
    .interest-card:hover { transform: translateY(-7px) scale(1.02) !important; }
    .interest-card .icon { filter: drop-shadow(0 0 16px rgba(139,124,255,.7)); }

    /* ---------- Project cards ---------- */
    .project-card { padding: 32px !important; }
    .project-card:before {
        width: 2px !important;
        background: var(--grad) !important;
        box-shadow: 0 0 22px rgba(139,124,255,.85);
    }
    .project-card:hover {
        transform: translateY(-6px);
        border-color: rgba(139,124,255,.4) !important;
        box-shadow: 0 26px 60px rgba(0,0,0,.6), 0 0 0 1px rgba(139,124,255,.22) !important;
    }
    .project-card h3 { color: var(--txt) !important; font-size: 1.4em !important; font-weight: 600; }
    .project-card:hover h3 {
        background: var(--grad);
        -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .project-card p { color: var(--txt-2) !important; }
    .project-date {
        background: rgba(255,255,255,.05) !important;
        border: 1px solid var(--stroke);
        color: var(--txt-3) !important;
        font-family: 'JetBrains Mono', monospace; font-size: .8em !important;
    }

    /* ---------- Project detail header ---------- */
    .project-detail-header {
        background: linear-gradient(135deg, rgba(139,124,255,.16), rgba(200,107,255,.08)) !important;
        border: 1px solid var(--stroke);
        border-radius: var(--radius) !important;
        position: relative; overflow: hidden;
        box-shadow: 0 20px 60px rgba(0,0,0,.45);
    }
    .project-detail-header::before {
        content:''; position:absolute; inset:0;
        background-image:
            linear-gradient(rgba(255,255,255,.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,.03) 1px, transparent 1px);
        background-size: 34px 34px;
    }
    .project-detail-header h1 {
        position: relative;
        background: linear-gradient(120deg,#fff 10%,#c9bfff 60%,#8fe9ff 100%);
        -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .project-meta-item {
        position: relative;
        background: rgba(0,0,0,.28);
        border: 1px solid var(--stroke);
        padding: 7px 15px; border-radius: 999px;
        font-size: .82em; color: var(--txt-2);
        font-family: 'JetBrains Mono', monospace;
    }
    .project-meta { gap: 12px !important; }

    /* ---------- Tech badges ---------- */
    .tech-badge-large {
        background: rgba(139,124,255,.09) !important;
        border: 1px solid rgba(139,124,255,.26);
        color: var(--txt) !important;
        font-size: .9em !important;
        font-weight: 500;
        transition: transform .3s cubic-bezier(.34,1.5,.64,1), box-shadow .3s, border-color .3s, background .3s;
        cursor: default;
    }
    .tech-badge-large:hover {
        transform: translateY(-4px) scale(1.04);
        background: rgba(139,124,255,.2) !important;
        border-color: rgba(200,107,255,.7);
        box-shadow: 0 10px 28px rgba(139,124,255,.4);
    }
    .tech-badge-large small { color: var(--txt-2) !important; }

    /* ---------- Screenshots ---------- */
    .screenshot-item {
        border: 1px solid var(--stroke);
        border-radius: 14px !important;
        background: rgba(0,0,0,.3);
        box-shadow: 0 14px 40px rgba(0,0,0,.5) !important;
        transition: transform .45s cubic-bezier(.34,1.25,.64,1), box-shadow .45s, border-color .45s;
    }
    .screenshot-item:hover {
        transform: translateY(-6px);
        border-color: rgba(139,124,255,.45);
        box-shadow: 0 26px 65px rgba(0,0,0,.65), 0 0 0 1px rgba(139,124,255,.2) !important;
    }
    .screenshot-item img { transition: filter .4s; }
    .screenshot-item:hover img { filter: brightness(1.06) saturate(1.08); }
    .screenshot-caption {
        background: rgba(255,255,255,.04) !important;
        color: var(--txt-2) !important;
        border-top: 1px solid var(--stroke);
        font-size: .9em;
    }

    /* ---------- Footer ---------- */
    footer {
        background: rgba(255,255,255,.02) !important;
        border-top: 1px solid var(--stroke);
        color: var(--txt-3) !important;
    }

    /* ---------- Neutralise remaining hardcoded light-mode inline colours ---------- */
    [style*="#333"], [style*="#444"], [style*="#555"], [style*="#666"], [style*="#999"] {
        color: var(--txt-2) !important;
    }
    .contact-card a { color: var(--neon) !important; }
    .contact-card a:hover { color: var(--cyan) !important; }

    /* ---------- Scroll reveal ---------- */
    html.js .reveal-target {
        opacity: 0;
        transform: translateY(30px);
        transition: opacity .75s cubic-bezier(.16,1,.3,1), transform .75s cubic-bezier(.16,1,.3,1);
    }
    html.js .reveal-target.is-visible { opacity: 1; transform: none; }

    /* ---------- Tab transition ---------- */
    .tab-content.active { animation: tabIn .55s cubic-bezier(.16,1,.3,1); }
    @keyframes tabIn {
        from { opacity:0; transform: translateY(16px) scale(.995); filter: blur(3px); }
        to   { opacity:1; transform:none; filter:none; }
    }

    /* ---------- Reduced motion ---------- */
    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after { animation-duration:.01ms !important; animation-iteration-count:1 !important; transition-duration:.01ms !important; }
        html.js .reveal-target { opacity:1 !important; transform:none !important; }
    }

    /* ---------- In-page PDF viewer ---------- */
    .pdf-modal {
        position: fixed; inset: 0; z-index: 6000;
        display: flex; align-items: center; justify-content: center;
        padding: 4vh 4vw;
        opacity: 0; pointer-events: none;
        transition: opacity .3s ease;
    }
    .pdf-modal.open { opacity: 1; pointer-events: auto; }
    .pdf-modal-backdrop {
        position: absolute; inset: 0;
        background: rgba(4,4,9,.82);
        backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
    }
    .pdf-modal-panel {
        position: relative;
        width: min(1020px, 100%); height: min(88vh, 100%);
        display: flex; flex-direction: column;
        background: rgba(14,14,22,.97);
        border: 1px solid var(--stroke-2);
        border-radius: 16px; overflow: hidden;
        box-shadow: 0 40px 120px rgba(0,0,0,.8), 0 0 0 1px rgba(139,124,255,.18);
        transform: translateY(26px) scale(.97);
        transition: transform .4s cubic-bezier(.16,1,.3,1);
    }
    .pdf-modal.open .pdf-modal-panel { transform: none; }
    .pdf-modal-bar {
        display: flex; align-items: center; justify-content: space-between; gap: 16px;
        padding: 13px 18px;
        border-bottom: 1px solid var(--stroke);
        background: rgba(255,255,255,.03);
    }
    .pdf-modal-title {
        font-family: 'Space Grotesk', sans-serif; font-weight: 600;
        font-size: .95em; color: var(--txt);
        overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
    }
    .pdf-modal-actions { display: flex; gap: 8px; flex-shrink: 0; }
    .pdf-icon-btn {
        width: 34px; height: 34px;
        display: grid; place-items: center;
        border-radius: 9px; cursor: pointer;
        background: rgba(255,255,255,.05);
        border: 1px solid var(--stroke);
        color: var(--txt-2); font-size: 15px; line-height: 1;
        text-decoration: none;
        transition: background .25s, border-color .25s, color .25s, transform .25s;
    }
    .pdf-icon-btn:hover {
        background: rgba(139,124,255,.22);
        border-color: rgba(200,107,255,.6);
        color: #fff; transform: translateY(-2px);
    }
    .pdf-frame { flex: 1; width: 100%; border: 0; background: #1b1b24; }

    /* ---------- Uniform screenshot grid ----------
       Every tile is the same size regardless of the source image's aspect
       ratio. `contain` letterboxes the odd ones out instead of cropping them,
       and the lightbox below lets you see any of them full size. */
    .screenshots-grid {
        grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)) !important;
        gap: 24px !important;
    }
    .screenshot-item {
        grid-column: auto !important;   /* neutralise the inline "1 / -1" spans */
        display: flex; flex-direction: column;
        cursor: zoom-in;
    }
    .screenshot-item img {
        width: 100% !important;
        max-width: none !important;
        margin: 0 !important;
        display: block !important;
        border-radius: 0 !important;
        aspect-ratio: 22 / 10;
        object-fit: contain;
        object-position: center;
        background: #0d0d14;
    }
    .screenshot-item .screenshot-caption { flex: 1; }

    /* ---------- Screenshot lightbox ---------- */
    .img-lightbox {
        position: fixed; inset: 0; z-index: 6500;
        display: flex; align-items: center; justify-content: center;
        padding: 5vh 5vw;
        opacity: 0; pointer-events: none;
        transition: opacity .3s ease;
    }
    .img-lightbox.open { opacity: 1; pointer-events: auto; }
    .img-lightbox-backdrop {
        position: absolute; inset: 0;
        background: rgba(3,3,7,.9);
        backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
    }
    .img-lightbox-fig {
        position: relative; margin: 0;
        max-width: 100%; max-height: 100%;
        display: flex; flex-direction: column; gap: 14px;
        transform: scale(.96); transition: transform .38s cubic-bezier(.16,1,.3,1);
    }
    .img-lightbox.open .img-lightbox-fig { transform: none; }
    .img-lightbox-fig img {
        max-width: 100%; max-height: 78vh;
        object-fit: contain;
        border-radius: 12px;
        border: 1px solid var(--stroke-2);
        box-shadow: 0 40px 120px rgba(0,0,0,.85);
        background: #0d0d14;
    }
    .img-lightbox-fig figcaption {
        text-align: center; color: var(--txt-2);
        font-size: .92em; line-height: 1.5;
        max-width: 900px; margin: 0 auto;
    }
    .img-lightbox-close {
        position: absolute; top: 22px; right: 26px;
        width: 42px; height: 42px;
        display: grid; place-items: center;
        border-radius: 11px; cursor: pointer;
        background: rgba(255,255,255,.07);
        border: 1px solid var(--stroke);
        color: var(--txt); font-size: 18px; line-height: 1;
        transition: background .25s, border-color .25s, transform .25s;
        z-index: 2;
    }
    .img-lightbox-close:hover {
        background: rgba(139,124,255,.28);
        border-color: rgba(200,107,255,.6);
        transform: translateY(-2px);
    }

    /* ---------- Mobile ---------- */
    @media (max-width: 968px) {
        .pdf-modal { padding: 0; }
        .pdf-modal-panel { width: 100%; height: 100%; border-radius: 0; border: none; }
        .nav-links {
            background: rgba(9,9,16,.97) !important;
            backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
            border-bottom: 1px solid var(--stroke);
        }
        .nav-links li a { border-bottom: 1px solid var(--stroke) !important; }
        .nav-links li a::after { display: none; }
        .dropdown-content { background: rgba(0,0,0,.4) !important; border:none; box-shadow:none !important; }
        .hero { padding: 44px 22px !important; }
        .cursor-glow { display: none; }
    }
    </style>
</head>
<body>
    <!-- Ambient layers -->
    <div class="scroll-progress" id="scrollProgress"></div>
    <div class="cursor-glow" id="cursorGlow"></div>
    <div class="bg-mesh" aria-hidden="true">
        <span class="blob b1"></span>
        <span class="blob b2"></span>
        <span class="blob b3"></span>
        <div class="grid-overlay"></div>
    </div>

    <!-- In-page certificate viewer -->
    <div class="pdf-modal" id="pdfModal" role="dialog" aria-modal="true" aria-label="Certificate viewer">
        <div class="pdf-modal-backdrop" data-close></div>
        <div class="pdf-modal-panel">
            <div class="pdf-modal-bar">
                <span class="pdf-modal-title" id="pdfModalTitle">Certificate</span>
                <div class="pdf-modal-actions">
                    <a class="pdf-icon-btn" id="pdfOpenNew" href="#" target="_blank" rel="noopener" title="Open in new tab">⇗</a>
                    <button class="pdf-icon-btn" type="button" data-close title="Close (Esc)">✕</button>
                </div>
            </div>
            <iframe class="pdf-frame" id="pdfFrame" title="Certificate PDF"></iframe>
        </div>
    </div>

    <!-- Screenshot lightbox -->
    <div class="img-lightbox" id="imgLightbox" role="dialog" aria-modal="true" aria-label="Screenshot viewer">
        <div class="img-lightbox-backdrop" data-imgclose></div>
        <button class="img-lightbox-close" type="button" data-imgclose title="Close (Esc)">✕</button>
        <figure class="img-lightbox-fig">
            <img id="imgLightboxImg" src="" alt="">
            <figcaption id="imgLightboxCap"></figcaption>
        </figure>
    </div>

    <!-- Navigation -->
    <nav>
        <div class="nav-container">
            <div class="logo">Aswinthmani V</div>
            <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">☰</button>
            <ul class="nav-links" id="navLinks">
                <li><a href="#" class="nav-link active" onclick="showTab(event, 'home')">Home</a></li>
                <li><a href="#" class="nav-link" onclick="showTab(event, 'about')">About</a></li>
                <li><a href="#" class="nav-link" onclick="showTab(event, 'education')">Education</a></li>
                <li><a href="#" class="nav-link" onclick="showTab(event, 'experience')">Experience</a></li>
                <li><a href="#" class="nav-link" onclick="showTab(event, 'skills')">Skills</a></li>
                <li class="dropdown">
                    <a href="#" class="nav-link" onclick="showTab(event, 'projects')">Projects ▾</a>
                    <div class="dropdown-content">
                        <a href="#" onclick="showTab(event, 'project-ami')">WhatsApp Financial Dashboard</a>
                        <a href="#" onclick="showTab(event, 'project-quote')">FinSight AI – Intelligent Financial Analysis Platform</a>
                        <a href="#" onclick="showTab(event, 'project-ticket')">Automated SIP Reminder & Client Communication System</a>
                        <a href="#" onclick="showTab(event, 'project-followup')">Smart Follow-up System</a>
                        <a href="#" onclick="showTab(event, 'project-proposal')">Proposal Generator</a>
                        <a href="#" onclick="showTab(event, 'project-youtube')">YouTube Sentiment Analysis</a>
                        <a href="#" onclick="showTab(event, 'project-face')">Face Authentication System</a>
                        <a href="#" onclick="showTab(event, 'project-portfolio')">Portfolio Tracker</a>
                        <a href="#" onclick="showTab(event, 'project-uci-pdf-cleanup')">PDF Cleanup</a>
                        <a href="#" onclick="showTab(event, 'project-orchid-msi')">MSI SharePoint Uploader</a>
                    </div>
                </li>
                <li><a href="#" class="nav-link" onclick="showTab(event, 'contact')">Contact</a></li>
            </ul>
        </div>
    </nav>

    <div class="container">
        <!-- Home Tab -->
        <div id="home" class="tab-content active">
            <div class="hero">
            <img src="{{ url_for('static', filename='images/profile.png') }}"  alt="Aswinthmani V" class="profile-photo"/>
                <h1>Aswinthmani V</h1>
                <p class="title">AI & Automation Engineer | FinTech & Backend Systems</p>
<p class="tagline">
Building production-grade AI and automation systems for real-world financial workflows,
from WhatsApp Cloud APIs to CRM-driven decision pipelines.
</p>
                <div class="contact-links">
                    <a href="mailto:aswinthmani10@gmail.com" class="contact-btn">📧 Email Me</a>
                    <a href="https://linkedin.com/in/aswinthmani-v-ab6852240" target="_blank" class="contact-btn">💼 LinkedIn</a>
                    <a href="https://github.com/Aswinthmani2003" target="_blank" class="contact-btn">🐙 GitHub</a>
                </div>
            </div>
            
            <div class="section">
    <h2>Profile</h2>

    <p style="font-size: 1.15em; line-height: 1.8; color: #444;">
        AI & Data Science undergraduate with hands-on experience building production-grade automation
        and AI systems for real-world business workflows. Specialized in backend development,
        API integrations, and AI-assisted decision systems used in live environments.
    </p>

    <ul style="margin-top: 20px; color: #555; line-height: 1.8;">
        <li>Built and deployed WhatsApp Cloud API–based financial automation systems used by a SEBI-registered firm</li>
        <li>Designed AI–human collaboration workflows with real-time monitoring and human takeover</li>
        <li>Strong backend foundation using Python, Flask, MongoDB, and REST APIs</li>
        <li>Experience working with real client data, compliance constraints, and production operations</li>
    </ul>

    <p style="margin-top: 20px; font-weight: 500; color: #666;">
    Interested in AI Engineering, Automation Engineering, and Backend roles,
    with a strong focus on AI-driven automation for financial operations, fintech platforms,
    and data-backed decision systems.
</p>

</div>

        </div>

        <!-- About Tab -->
        <div id="about" class="tab-content">
            <div class="section">
                <h2>About Me</h2>
                <div class="about-content">
                    <div class="about-text">
                        <p>
                            I am an Associate Software Developer at Solartis LLC, working on AI-driven solutions and scalable backend systems for enterprise applications.
                        </p>
                        <p>
                            My work focuses on automation, API integrations, and production-grade systems that support real-world business workflows.
                            I specialize in backend development, AI-assisted decision systems, and building reliable data-driven applications.
                        </p>
                        <p>
                            I am particularly interested in AI engineering, automation systems, and backend architecture, where intelligent systems improve operational efficiency and decision-making at scale.
                        </p>
                    </div>
                    <div class="about-highlights">
                        <h3>Quick Facts</h3>
                        <ul>
                            <li>CGPA: 8.0/10</li>
                            <li>AWS Certified (ML & Cloud)</li>
                            <li>8+ Major Projects Completed</li>
                            <li>Experienced in Production Systems</li>
                            <li>Based in Chennai, India</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>Interests & Hobbies</h2>
                <div class="interests-grid">
                    <div class="interest-card">
                        <div class="icon">🤖</div>
                        <h3>Exploring AI Tools</h3>
                    </div>
                    <div class="interest-card">
                        <div class="icon">🧠</div>
                        <h3>Machine Learning</h3>
                    </div>
                    <div class="interest-card">
                        <div class="icon">⚽</div>
                        <h3>Competitive Sports</h3>
                    </div>
                    <div class="interest-card">
                        <div class="icon">💪</div>
                        <h3>Fitness Enthusiast</h3>
                    </div>
                </div>
            </div>
        </div>

        <!-- Education Tab -->
        <div id="education" class="tab-content">
            <div class="section">
                <h2>Education</h2>
                <div class="education-card">
                    <h3>Sri Ramachandra Institute of Higher Education and Research</h3>
                    <p class="degree">B.Tech in Artificial Intelligence and Data Analytics</p>
                    <div class="education-details">
                        <div class="education-detail-item">
                            <strong>Duration</strong>
                            <p>Aug 2021 - Jun 2025</p>
                        </div>
                        <div class="education-detail-item">
                            <strong>CGPA</strong>
                            <p>8.0 / 10.0</p>
                        </div>
                        <div class="education-detail-item">
                            <strong>Location</strong>
                            <p>Chennai, Tamil Nadu</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>Certifications</h2>
                <div class="skills-grid">
                    <div class="skill-card">
                        <h3>📜 NISM Mutual Fund Distributors Certification</h3>
                        <p style="color: #555; margin-top: 10px;">
                            Certified by the National Institute of Securities Markets (NISM) in Mutual Fund Distribution — Issued Feb 2026, Valid through Feb 2029
                        </p>
                        <a href="/static/certificates/Mutual%20Fund%20Distributors%20Certification%20Examination.pdf" target="_blank" class="cert-btn">📄 View Certificate</a>
                    </div>
                    <div class="skill-card">
                        <h3>☁️ Oracle Cloud Infrastructure 2025 Certified Foundations Associate</h3>
                        <p style="color: #555; margin-top: 10px;">
                            Foundational knowledge of Oracle Cloud Infrastructure services, core concepts, and cloud computing fundamentals
                        </p>
                        <a href="/static/certificates/Oracle%20Cloud%20Infrastructure%202025%20Certified%20Foundations%20Associate.pdf" target="_blank" class="cert-btn">📄 View Certificate</a>
                    </div>
                    <div class="skill-card">
                        <h3>☁️ Oracle AI Vector Search Certified Professional</h3>
                        <p style="color: #555; margin-top: 10px;">
                            Expertise in vector databases, similarity search, embeddings, and AI-powered semantic retrieval using Oracle AI Vector Search
                        </p>
                        <a href="/static/certificates/Oracle%20AI%20Vector%20Search%20Certified%20Professional.pdf" target="_blank" class="cert-btn">📄 View Certificate</a>
                    </div>
                    <div class="skill-card">
                        <h3>☁️ Oracle Cloud Infrastructure (OCI) 2025 – AI Foundations Associate</h3>
                        <p style="color: #555; margin-top: 10px;">
                            Strong foundation in AI concepts, OCI services, model lifecycle, and enterprise AI deployment fundamentals
                        </p>
                        <a href="/static/certificates/Oracle%20Cloud%20Infrastructure%202025%20Certified%20AI%20Foundations%20Associate.pdf" target="_blank" class="cert-btn">📄 View Certificate</a>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Experience Tab -->
<div id="experience" class="tab-content">
    <div class="section">
        <h2>Experience</h2>

        <div class="project-card">
            <div class="project-header">
                <h3>Associate Software Engineer — Solartis LLC</h3>
                <span class="project-date">Feb 2026 – Present</span>
            </div>
            <p>
                Working on AI-driven automation solutions and intelligent workflow systems for enterprise applications, with a focus on integrating AI capabilities into existing business processes.
            </p>
            <ul style="margin-top: 10px; color: #555;">
                <li>Developing and implementing AI-powered automation solutions to streamline complex business workflows and improve operational efficiency</li>
                <li>Building intelligent systems that integrate AI layers with existing enterprise applications using n8n workflow automation</li>
                <li>Working with cutting-edge AI tools including Claude Code for advanced code generation and RAG (Retrieval-Augmented Generation) systems for enhanced AI responses</li>
                <li>Designing and deploying scalable automation pipelines that leverage AI capabilities to reduce manual intervention and accelerate business processes</li>
                <li>Collaborating on production-grade systems that combine traditional backend development with modern AI/ML technologies</li>
            </ul>
        </div>

        <div class="project-card">
            <div class="project-header">
                <h3>Associate Software Engineer Intern — Solartis LLC</h3>
                <span class="project-date">Aug 2025 – Jan 2026</span>
            </div>
            <p>
                Contributed to automation infrastructure and AI integration projects, gaining hands-on experience with enterprise-scale workflow automation and intelligent system design.
            </p>
            <ul style="margin-top: 10px; color: #555;">
                <li>Assisted in developing automation workflows using n8n and integrating AI capabilities into business processes</li>
                <li>Gained practical experience with RAG systems and AI-assisted development tools like Claude Code</li>
                <li>Worked on improving existing automation pipelines and identifying opportunities for AI enhancement</li>
            </ul>
        </div>

        <div class="project-card">
            <div class="project-header">
                <h3>AIML / Automation Intern — App Synergies</h3>
                <span class="project-date">Feb 2025 – Jul 2025</span>
            </div>
            <p>
                Worked on production-grade automation and AI systems involving WhatsApp Cloud API, CRM workflows,
                and real-time dashboards for business operations.
            </p>
            <ul style="margin-top: 10px; color: #555;">
                <li>Developed an AI-driven system for sales teams, automating lead qualification, meeting scheduling, and follow-ups, with integrated time zone intelligence and regional routing</li>
                <li>Built an open-source proposal generator that automates professional proposal creation with dynamic templates, integrating Google Cloud for deployment and document generation</li>
                <li>Worked with real client data, maintained automation pipelines, implemented real-time monitoring, and handled production constraints</li>
            </ul>
        </div>

        <div class="project-card">
            <div class="project-header">
                <h3>Full Stack Developer Intern — LIA Infraservices</h3>
                <span class="project-date">Feb 2023 – Apr 2023</span>
            </div>
            <p>
                Focused on building a finance website replica with backend-driven calculations, data integration, and realistic investment workflows.
            </p>
            <ul style="margin-top: 10px; color: #555;">
                <li>Developed a Flask-based web application with user sign-in/login, portfolio dashboards, and investment calculators</li>
                <li>Implemented server-side logic for SIP and investment return calculations to simulate real-world wealth management scenarios</li>
                <li>Integrated the Polygon API to fetch and display stock market data, applying backend API handling and data processing concepts</li>
            </ul>
        </div>
    </div>
</div>


        <!-- Skills Tab -->
        <div id="skills" class="tab-content">
            <div class="section">
                <h2>Technical Skills</h2>
                <div class="skills-grid">
                    <div class="skill-card">
                        <h3>💻 Programming Languages</h3>
                        <ul>
                            <li>Python</li>
                            <li>SQL (MySQL)</li>
                            <li>JavaScript</li>
                            <li>Bash / Shell Scripting</li>
                            <li>HTML</li>
                            <li>CSS</li>
                        </ul>
                    </div>
                    <div class="skill-card">
                        <h3>🛠️ Frameworks & Libraries</h3>
                        <ul>
                            <li>Flask</li>
                            <li>Streamlit</li>
                            <li>Bootstrap</li>
                            <li>Web Scraping</li>
                        </ul>
                    </div>
                    <div class="skill-card">
                        <h3>🔧 Tools & Technologies</h3>
                        <ul>
                            <li>MongoDB</li>
                            <li>Selenium</li>
                            <li>Make.com</li>
                            <li>Zoho CRM (Automation, Custom Modules, API Integration)</li>
                            <li>N8N</li>
                            <li>ManyChats</li>
                            <li>Retell AI</li>
                            <li>Kubernetes</li>
                            <li>Git</li>
                        </ul>
                    </div>
                    <div class="skill-card">
                        <h3>🎯 Core Areas</h3>
                        <ul>
                            <li>Data Analysis</li>
                            <li>Financial Analytics</li>
                            <li>Machine Learning</li>
                            <li>Automation</li>
                            <li>Natural Language Processing</li>
                            <li>Computer Vision</li>
                            <li>LLM Integration</li>
                        </ul>
                    </div>
                    <div class="skill-card">
                        <h3>🤖📊 AI-Driven Data & Analytics</h3>
                        <ul>
                            <li>Exploratory Data Analysis (EDA)</li>
                            <li>Financial Data Analysis</li>
                            <li>LLM Integration & Prompt Engineering</li>
                            <li>AI-Generated Insight Pipelines</li>
                            <li>Conversational AI Systems</li>
                        </ul>
                    </div>
                    <div class="skill-card">
                        <h3>☁️ Cloud & APIs</h3>
                        <ul>
                            <li>Google Cloud Platform</li>
                            <li>WhatsApp Cloud API</li>
                            <li>RESTful APIs</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- Projects Overview Tab -->
        <div id="projects" class="tab-content">
            <div class="section">
                <h2>Projects Overview</h2>
                <p style="font-size: 1.1em; color: #555; margin-bottom: 30px;">
                    Click on any project to view detailed information, features, and screenshots.
                </p>
                
                <div class="project-card" onclick="showTab(event, 'project-ami')">
                    <div class="project-header">
                        <h3>WhatsApp-Based Financial Operations Dashboard</h3>
                        <span class="project-date">Dec 2025 - Mar 2026</span>
                    </div>
                    <p>Production-grade WhatsApp Cloud API dashboard for AI chatbot monitoring and financial client management.</p>
                    <span class="view-details-btn">View Details →</span>
                </div>
                
                <div class="project-card" onclick="showTab(event, 'project-quote')">
                    <div class="project-header">
                        <h3>FinSight AI – Intelligent Financial Analysis Platform</h3>
                        <span class="project-date">Jan 2026</span>
                    </div>
                    <p>AI-powered web application that analyzes bank statement CSVs to generate spending insights, interactive dashboards, and downloadable financial reports using LLMs.</p>
                    <span class="view-details-btn">View Details →</span>
                </div>
                
                <div class="project-card" onclick="showTab(event, 'project-ticket')">
                    <div class="project-header">
                        <h3>Automated SIP Reminder & Client Communication System</h3>
                        <span class="project-date">Nov 2025</span>
                    </div>
                    <p>Automated WhatsApp-based system to send compliant SIP debit reminders by integrating Zoho CRM, Make.com, and WhatsApp Cloud API.</p>
                    <span class="view-details-btn">View Details →</span>
                </div>
                
                <div class="project-card" onclick="showTab(event, 'project-followup')">
                    <div class="project-header">
                        <h3>Smart Global Follow-up System</h3>
                        <span class="project-date">May 2025 - Jun 2025</span>
                    </div>
                    <p>Automated client call flow with time zone-based scheduling and lead qualification.</p>
                    <span class="view-details-btn">View Details →</span>
                </div>

                <div class="project-card" onclick="showTab(event, 'project-proposal')">
                    <div class="project-header">
                        <h3>Proposal Generator</h3>
                        <span class="project-date">Feb 2025 - Mar 2025</span>
                    </div>
                    <p>Open-source Python tools for generating professional proposals with dynamic templates.</p>
                    <span class="view-details-btn">View Details →</span>
                </div>
            
                <div class="project-card" onclick="showTab(event, 'project-youtube')">
                    <div class="project-header">
                        <h3>YouTube Comment Sentiment Analysis</h3>
                        <span class="project-date">Oct 2024</span>
                    </div>
                    <p>Real-time sentiment analyzer for YouTube comments with web scraping and NLP.</p>
                    <span class="view-details-btn">View Details →</span>
                </div>

                <div class="project-card" onclick="showTab(event, 'project-face')">
                    <div class="project-header">
                        <h3>Face Authentication System</h3>
                        <span class="project-date">Aug 2023 - Oct 2023</span>
                    </div>
                    <p>End-to-end facial authentication system for banking web applications.</p>
                    <span class="view-details-btn">View Details →</span>
                </div>

                <div class="project-card" onclick="showTab(event, 'project-portfolio')">
                    <div class="project-header">
                        <h3>Investment Portfolio Tracker</h3>
                        <span class="project-date">Feb 2023 - Apr 2023</span>
                    </div>
                    <p>Flask-based finance web application with real-time market data and investment calculators.</p>
                    <span class="view-details-btn">View Details →</span>
                </div>

                <div class="project-card" onclick="showTab(event, 'project-uci-pdf-cleanup')">
                    <div class="project-header">
                        <h3>Automated PDF Temp Cleanup System</h3>
                        <span class="project-date">Jul 2026 - Present</span>
                    </div>
                    <p>Reusable automated cleanup system for temporary PDF/Word files across UCI, UAT, and PROD environments — with AI-generated summaries, Teams Adaptive Cards, and email reports via an n8n + Flask REST API pipeline.</p>
                    <span class="view-details-btn">View Details →</span>
                </div>

                <div class="project-card" onclick="showTab(event, 'project-orchid-msi')">
                    <div class="project-header">
                        <h3>Orchid MSI SharePoint Upload Automation</h3>
                        <span class="project-date">May 2026 - Jul 2026</span>
                    </div>
                    <p>End-to-end automation pipeline that polls MySQL for completed MSI batches, transfers files via SFTP, verifies PDFs, and uploads to SharePoint — eliminating daily manual effort entirely.</p>
                    <span class="view-details-btn">View Details →</span>
                </div>
            </div>
        </div>

        <!-- Project Detail Pages -->
        
        <!-- Project 1: AMI ClientConnect -->
        <div id="project-ami" class="tab-content">
            <a href="#" class="back-button" onclick="showTab(event, 'projects')">← Back to Projects</a>
            
            <div class="project-detail-header">
                <h1>WhatsApp-Based Financial Operations Dashboard</h1>
                <p style="font-size: 1.2em; margin-top: 10px;">AMI ClientConnect</p>
                <div class="project-meta">
                    <div class="project-meta-item">
                        <span>📅</span>
                        <span>Dec 2025 - Mar 2026</span>
                    </div>
                    <div class="project-meta-item">
                        <span>🏢</span>
                        <span>Production System</span>
                    </div>
                    <div class="project-meta-item">
                        <span>👥</span>
                        <span>SEBI-Registered Client</span>
                    </div>
                </div>
            </div>

            <div class="project-overview">
                <h2>Project Overview</h2>
                <p>
                    Built a production-grade WhatsApp Cloud API dashboard to monitor AI chatbot conversations, enable human takeover, 
                    and manage follow-ups in real time for a SEBI-registered mutual fund distributor. This system revolutionizes 
                    how financial advisors interact with their clients by providing seamless AI-human collaboration.
                </p>
                <p>
                    The dashboard handles multiple clients simultaneously, provides real-time conversation monitoring, and ensures 
                    that no high-intent investment opportunity is missed through intelligent notification systems and workflow automation.
                </p>
                
                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Key Features</h3>
                <div class="features-grid">
                    <div class="feature-card">
                        <h3>🤖 AI Chatbot Integration</h3>
                        <p>GPT-4 powered conversational AI that handles client inquiries, provides SIP data, and qualifies leads automatically.</p>
                    </div>
                    <div class="feature-card">
                        <h3>👤 Human Takeover</h3>
                        <p>Seamless transition from AI to human agent when complex queries arise or high-value clients need personalized attention.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📊 Real-time Monitoring</h3>
                        <p>Live dashboard showing all active conversations, client details, and conversation history with instant notifications.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🔄 Multi-Client Management</h3>
                        <p>Handle conversations with multiple clients simultaneously with organized threading and context preservation.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📁 File Management</h3>
                        <p>Secure sending and receiving of documents, reports, and financial statements through WhatsApp.</p>
                    </div>
                    <div class="feature-card">
                        <h3>⚙️ Chatbot Controls</h3>
                        <p>ON/OFF toggle for AI chatbot, allowing manual control over automation levels during business hours.</p>
                    </div>
                </div>

                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Technologies Used</h3>
                <div class="tech-stack-detail">
                    <span class="tech-badge-large">WhatsApp Cloud API <small style="font-weight:400; opacity:0.85; font-size:0.78em">— sends &amp; receives messages</small></span>
                    <span class="tech-badge-large">Python <small style="font-weight:400; opacity:0.85; font-size:0.78em">— backend logic</small></span>
                    <span class="tech-badge-large">Flask <small style="font-weight:400; opacity:0.85; font-size:0.78em">— web server &amp; routes</small></span>
                    <span class="tech-badge-large">MongoDB <small style="font-weight:400; opacity:0.85; font-size:0.78em">— stores conversations</small></span>
                    <span class="tech-badge-large">JavaScript <small style="font-weight:400; opacity:0.85; font-size:0.78em">— dashboard UI</small></span>
                    <span class="tech-badge-large">Make.com <small style="font-weight:400; opacity:0.85; font-size:0.78em">— workflow automation</small></span>
                    <span class="tech-badge-large">GPT-4 <small style="font-weight:400; opacity:0.85; font-size:0.78em">— AI chatbot responses</small></span>
                </div>
            </div>

            <div class="screenshots-section">
                <h2>Screenshots & Demo</h2>
                <div class="screenshots-grid">
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/Dashboard_UI.png') }}"  alt="AMI Dashboard" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Main Dashboard Interface.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/Customer_Interaction.png') }}"  alt="AMI Dashboard" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Real-time Conversation Monitoring.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/Dashboard_User.png') }}"  alt="AMI Dashboard" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Scenario of Human taking up the conversatione.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/filter.png') }}"  alt="AMI Dashboard" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Dashboard's Filter Section.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/Notification.png') }}"  alt="AMI Dashboard" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Unread Message Notification.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/client_pov.jpg') }}"  alt="AMI Dashboard" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">End-to-end WhatsApp interaction where an AI assistant handles client queries, escalates to a human advisor, and securely delivers fund statements as PDF.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/my_pov.jpg') }}"  alt="AMI Dashboard" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Real-time operations dashboard enabling human takeover, conversation monitoring, and document delivery for a production WhatsApp Cloud API financial assistant.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/my_pov1.png') }}"  alt="AMI Dashboard" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Custom WhatsApp Cloud API dashboard delivering real-time SIP details to clients using CRM-integrated data.</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Project 2: Proposal Generator -->
        <div id="project-proposal" class="tab-content">
            <a href="#" class="back-button" onclick="showTab(event, 'projects')">← Back to Projects</a>
            
            <div class="project-detail-header">
                <h1>Proposal Generator</h1>
                <p style="font-size: 1.2em; margin-top: 10px;">Technology & Digital Marketing</p>
                <div class="project-meta">
                    <div class="project-meta-item">
                        <span>📅</span>
                        <span>Feb 2025 - Mar 2025</span>
                    </div>
                    <div class="project-meta-item">
                        <span>🔓</span>
                        <span>Open Source</span>
                    </div>
                </div>
            </div>

            <div class="project-overview">
                <h2>Project Overview</h2>
                <p>
                    Developed two open-source Python tools for generating professional proposals with dynamic templates. These tools 
                    streamline the proposal creation process for consultants, service providers, and digital marketing agencies.
                </p>
                
                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Key Features</h3>
                <div class="features-grid">
                    <div class="feature-card">
                        <h3>📝 Dynamic Templates</h3>
                        <p>Customizable proposal templates that adapt to different business needs and client requirements.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🤖 Automated Generation</h3>
                        <p>Automatically populate proposals with client data, project details, and pricing information.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📊 GCP Integration</h3>
                        <p>Cloud-based document generation and storage using Google Cloud Platform services.</p>
                    </div>
                </div>

                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Technologies Used</h3>
                <div class="tech-stack-detail">
                    <span class="tech-badge-large">Python <small style="font-weight:400; opacity:0.85; font-size:0.78em">— template processing logic</small></span>
                    <span class="tech-badge-large">Streamlit <small style="font-weight:400; opacity:0.85; font-size:0.78em">— initial prototype &amp; UI</small></span>
                    <span class="tech-badge-large">Google Cloud Platform <small style="font-weight:400; opacity:0.85; font-size:0.78em">— final deployment &amp; hosting</small></span>
                    <span class="tech-badge-large">Document Automation <small style="font-weight:400; opacity:0.85; font-size:0.78em">— dynamic proposal generation</small></span>
                </div>
            </div>

            <div class="screenshots-section">
                <h2>Screenshots & Demo</h2>
                <div class="screenshots-grid">
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/gen_ui.png') }}"  alt="AMI Dashboard" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Proposal Generational Interface</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/gen_select.png') }}"  alt="AMI Dashboard" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Template Selection Screen</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/gen_bef.png') }}"  alt="AMI Dashboard" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">After giving the details and generate the document</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/gen_aft.png') }}"  alt="AMI Dashboard" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Downloading the Generated Document</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/gen_output.png') }}"  alt="AMI Dashboard" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">The Generated Document</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Project 3: Smart Follow-up System -->
        <div id="project-followup" class="tab-content">
            <a href="#" class="back-button" onclick="showTab(event, 'projects')">← Back to Projects</a>
            
            <div class="project-detail-header">
                <h1>Smart Global Follow-up System</h1>
                <p style="font-size: 1.2em; margin-top: 10px;">Lead Qualification & Scheduling</p>
                <div class="project-meta">
                    <div class="project-meta-item">
                        <span>📅</span>
                        <span>May 2025 - Jun 2025</span>
                    </div>
                    <div class="project-meta-item">
                        <span>🌍</span>
                        <span>Global System</span>
                    </div>
                </div>
            </div>

            <div class="project-overview">
                <h2>Project Overview</h2>
                <p>
                    Smart Global Follow-up System automates AI-driven lead qualification, regional routing, and time-zone–aware meeting scheduling using Retell AI, Make.com, and CRM workflows. It converts voice conversations into structured CRM updates, auto-books calendar meetings, and triggers multi-channel reminders, eliminating manual follow-ups across global sales operations.
                </p>
                
                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Key Features</h3>
                <div class="features-grid">
                    <div class="feature-card">
                        <h3>🎙️ AI Voice Calls</h3>
                        <p>Retell AI conducts natural conversations to qualify leads and gather project requirements.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🌏 Time Zone Intelligence</h3>
                        <p>Automatic scheduling that respects different time zones for global client base.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📅 Calendar Integration</h3>
                        <p>Seamless integration with Google Calendar and Microsoft Teams for meeting management.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🔔 Automated Reminders</h3>
                        <p>Region-specific follow-up agents send reminders through Make.com workflows.</p>
                    </div>
                </div>

                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Technologies Used</h3>
                <div class="tech-stack-detail">
                    <span class="tech-badge-large">Retell AI <small style="font-weight:400; opacity:0.85; font-size:0.78em">— AI voice calling agent</small></span>
                    <span class="tech-badge-large">Make.com <small style="font-weight:400; opacity:0.85; font-size:0.78em">— orchestrates the full flow</small></span>
                    <span class="tech-badge-large">Google Calendar <small style="font-weight:400; opacity:0.85; font-size:0.78em">— time-zone-aware scheduling</small></span>
                    <span class="tech-badge-large">Microsoft Teams <small style="font-weight:400; opacity:0.85; font-size:0.78em">— team notifications</small></span>
                </div>
            </div>

            <div class="screenshots-section">
                <h2>Screenshots & Demo</h2>
                <div class="screenshots-grid">
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/fo_1.jpg') }}"  alt="Follow-up Call" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Qualified leads are automatically scheduled into Google Calendar with correct time-zone handling and video meeting links.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/fo_2.jpg') }}"  alt="Follow-up Call" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">AI call insights captured as structured webhook data to drive automated routing, CRM updates, and meeting scheduling.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/fo_3.jpg') }}"  alt="Follow-up Call" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Rule-based routing filters evaluate lead status, country code, and call attempts to direct each lead to the correct regional follow-up workflow.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/fo_4.jpg') }}"  alt="Follow-up Call" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Independent region-specific follow-up agents handle localized scheduling and workflows, selected dynamically based on lead country code.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/fo_5.jpg') }}"  alt="Follow-up Call" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Lead status is automatically updated in CRM to reflect scheduled calls, ensuring a clean and accurate sales pipeline without manual intervention.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/fo_6.jpg') }}"  alt="Follow-up Call" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Real-time internal notifications are triggered with meeting details and lead context to keep teams aligned and prepared.</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Project 4: Automated SIP Reminder & Client Communication System -->
        <div id="project-ticket" class="tab-content">
            <a href="#" class="back-button" onclick="showTab(event, 'projects')">← Back to Projects</a>
            
            <div class="project-detail-header">
                <h1>Automated SIP Reminder & Client Communication System</h1>
                <div class="project-meta">
                    <div class="project-meta-item">
                        <span>📅</span>
                        <span>Nov 2025</span>
                    </div>
                    <div class="project-meta-item">
                        <span>💳</span>
                        <span>FinTech Automation</span>
                    </div>
                </div>
            </div>

            <div class="project-overview">
                <h2>Project Overview</h2>
                <p>
                    Built an automated SIP reminder and client communication system for a SEBI-registered mutual fund distributor to ensure timely debit notifications and reduce missed SIPs. The system integrates Zoho CRM as the source of truth, orchestrates workflows using Make.com, and delivers compliant utility messages via WhatsApp Cloud API, with fallback email notifications and delivery tracking through Meta WhatsApp Manager.
                </p>
                
                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Key Features</h3>
                <div class="features-grid">
                    <div class="feature-card">
                        <h3>🎯 Automated SIP Reminder Scheduling</h3>
                        <p>Triggers SIP debit reminders (1-day and 2-day prior) based on SIP due dates sourced from Zoho CRM.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📊 WhatsApp Utility Message Delivery</h3>
                        <p>Sends compliant WhatsApp utility templates via WhatsApp Cloud API, enabling notifications beyond the 24-hour session window.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🖥️ Parallel Multi-Channel Notifications</h3>
                        <p>Delivers SIP reminders via WhatsApp and email simultaneously to ensure timely client awareness.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🔍 CRM-Driven Workflow Orchestration</h3>
                        <p>Uses Zoho CRM as the source of truth with Make.com orchestrating scheduling, routing, and message dispatch workflows.</p>
                    </div>
                </div>

                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Technologies Used</h3>
                <div class="tech-stack-detail">
                    <span class="tech-badge-large">WhatsApp Cloud API <small style="font-weight:400; opacity:0.85; font-size:0.78em">— delivers SIP reminder messages</small></span>
                    <span class="tech-badge-large">Meta WhatsApp Manager <small style="font-weight:400; opacity:0.85; font-size:0.78em">— template approval &amp; management</small></span>
                    <span class="tech-badge-large">Zoho CRM <small style="font-weight:400; opacity:0.85; font-size:0.78em">— source of client data</small></span>
                    <span class="tech-badge-large">Make.com <small style="font-weight:400; opacity:0.85; font-size:0.78em">— orchestrates the full flow</small></span>
                    <span class="tech-badge-large">ManyChats <small style="font-weight:400; opacity:0.85; font-size:0.78em">— earlier version of the WhatsApp flow</small></span>
                    <span class="tech-badge-large">REST APIs &amp; Webhooks <small style="font-weight:400; opacity:0.85; font-size:0.78em">— connects all services</small></span>
                </div>
            </div>

            <div class="screenshots-section">
                <h2>Screenshots & Demo</h2>
                <div class="screenshots-grid">
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/r_1.jpg') }}"  alt="Sip Remainder" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">End-to-end workflow orchestrating SIP data retrieval from Zoho CRM and scheduled notification delivery.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/r_2.jpg') }}"  alt="Sip Remainder" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Utility message delivery, usage metrics, and cost tracking monitored through Meta WhatsApp Manager.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1; justify-self: center;">
                        <img  src="{{ url_for('static', filename='images/r_3.jpg') }}"  alt="Sip Remainder" style="width:50%; margin:0 auto; display:block; border-radius:14px;"">
                        <div class="screenshot-caption">Automated SIP debit reminder sent via WhatsApp with masked bank details and due-date information.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/r_4.jpg') }}"  alt="Sip Remainder" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Simultaneous email notification delivering detailed SIP and debit information to clients.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/r_5.jpg') }}"  alt="Sip Remainder" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Pre-approved WhatsApp utility templates configured for compliant SIP reminder communication.</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Project 2: FinSight AI -->
        <div id="project-quote" class="tab-content">
            <a href="#" class="back-button" onclick="showTab(event, 'projects')">← Back to Projects</a>
            
            <div class="project-detail-header">
                <h1>FinSight AI – Intelligent Financial Analysis Platform</h1>
                <div class="project-meta">
                    <div class="project-meta-item">
                        <span>📅</span>
                        <span>January 2026</span>
                    </div>
                    <div class="project-meta-item">
                        <span>🤖</span>
                        <span>AI · FinTech · Full-Stack</span>
                    </div>
                </div>
            </div>

            <div class="project-overview">
                <h2>Project Overview</h2>
                <p>
                    Built an AI-powered financial analysis system that processes CSV bank statements to automatically categorize transactions, visualize spending patterns, and generate actionable insights using large language models. Implemented an end-to-end pipeline covering data parsing, expense aggregation, conversational querying, and PDF report generation, with a clean web interface for interactive analysis.
                </p>
                
                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Key Features</h3>
                <div class="features-grid">
                    <div class="feature-card">
                        <h3>📂 CSV Bank Statement Upload</h3>
                        <p>Upload raw bank transaction files for instant analysis.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📊 Automated Expense Categorization</h3>
                        <p>Transactions are classified into meaningful spending categories using AI.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📈 Interactive Dashboards</h3>
                        <p>Visual breakdowns of spending by category and budget comparisons.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🤖 AI Financial Insights</h3>
                        <p>LLM-generated observations highlighting overspending and trends.</p>
                    </div>
                    <div class="feature-card">
                        <h3>💬 Conversational AI Assistant</h3>
                        <p>Ask natural language questions about your spending behavior.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📄 Downloadable PDF Report</h3>
                        <p>Auto-generated financial summary for offline review or sharing.</p>
                    </div>
                </div>

                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Technologies Used</h3>
                <div class="tech-stack-detail">
                    <span class="tech-badge-large">🐍 Flask (Python) <small style="font-weight:400; opacity:0.85; font-size:0.78em">— handles CSV uploads &amp; routes</small></span>
                    <span class="tech-badge-large">🧠 Groq API + Llama 3.3 <small style="font-weight:400; opacity:0.85; font-size:0.78em">— generates spending insights</small></span>
                    <span class="tech-badge-large">🌐 HTML, CSS, JavaScript <small style="font-weight:400; opacity:0.85; font-size:0.78em">— user interface</small></span>
                    <span class="tech-badge-large">📊 Chart.js <small style="font-weight:400; opacity:0.85; font-size:0.78em">— interactive spending charts</small></span>
                    <span class="tech-badge-large">📄 ReportLab <small style="font-weight:400; opacity:0.85; font-size:0.78em">— downloadable PDF export</small></span>
                </div>
            </div>

            <div class="screenshots-section">
                <h2>Screenshots & Demo</h2>
                <div class="screenshots-grid">
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/f1.png') }}"  alt="FinSight AI" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">High-level financial dashboard showing total spending, number of categories, and transaction volume derived from uploaded bank data.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/f2.png') }}"  alt="FinSight AI" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">AI-generated insights highlighting overspending patterns and actionable recommendations based on transaction analysis.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/f3.png') }}"  alt="FinSight AI" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Automatically categorized transaction ledger with dates, descriptions, spending categories, and amounts.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/f4.png') }}"  alt="FinSight AI" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Conversational AI assistant that answers user queries about spending behavior and budget deviations in natural language.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/f5.png') }}"  alt="FinSight AI" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Auto-generated PDF financial report summarizing spending, category breakdowns, and AI insights for offline review.</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Project 6: YouTube Sentiment Analysis -->
        <div id="project-youtube" class="tab-content">
            <a href="#" class="back-button" onclick="showTab(event, 'projects')">← Back to Projects</a>
            
            <div class="project-detail-header">
                <h1>YouTube Comment Sentiment Analysis</h1>
                <div class="project-meta">
                    <div class="project-meta-item">
                        <span>📅</span>
                        <span>Oct 2024</span>
                    </div>
                    <div class="project-meta-item">
                        <span>📊</span>
                        <span>NLP Analysis</span>
                    </div>
                </div>
            </div>

            <div class="project-overview">
                <h2>Project Overview</h2>
                <p>
                    Automated sentiment analysis pipeline that scrapes YouTube comments using Selenium and classifies them into positive, negative, or neutral categories using TextBlob to analyze audience feedback.
                </p>
                
                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Key Features</h3>
                <div class="features-grid">
                    <div class="feature-card">
                        <h3>🌐 Web Scraping</h3>
                        <p>Automated scraping of dynamically loaded YouTube comments using Selenium, handling scroll-based content loading.</p>
                    </div>
                    <div class="feature-card">
                        <h3>😊😐😞 Sentiment Classification</h3>
                        <p>Classifies comments into Positive, Negative, or Neutral categories using TextBlob.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🔄 Automated Processing</h3>
                        <p>Automatically processes scraped YouTube comments through cleaning, sentiment labeling, and dataset generation.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📈 Analytics Dashboard</h3>
                        <p>Dashboard visualizing the distribution of positive, neutral, and negative sentiments in scraped YouTube comments.</p>
                    </div>
                </div>

                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Technologies Used</h3>
                <div class="tech-stack-detail">
                    <span class="tech-badge-large">Python <small style="font-weight:400; opacity:0.85; font-size:0.78em">— scraping &amp; analysis logic</small></span>
                    <span class="tech-badge-large">Selenium <small style="font-weight:400; opacity:0.85; font-size:0.78em">— scrapes YouTube comments</small></span>
                    <span class="tech-badge-large">TextBlob <small style="font-weight:400; opacity:0.85; font-size:0.78em">— sentiment scoring</small></span>
                    <span class="tech-badge-large">NLP <small style="font-weight:400; opacity:0.85; font-size:0.78em">— text classification pipeline</small></span>
                </div>
            </div>

            <div class="screenshots-section">
                <h2>Screenshots & Demo</h2>
                <div class="screenshots-grid">
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/sa_1.png') }}"  alt="Sentiment Analysis" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Sample output of scraped YouTube comments with sentiment labels generated using TextBlob after preprocessing.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/sa_2.png') }}"  alt="Sentiment Analysis" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Distribution of positive, neutral, and negative sentiments across scraped YouTube comments.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/sa_3.png') }}"  alt="Sentiment Analysis" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Interactive sentiment classification of user-provided text using TextBlob polarity analysis.</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Project 7: Face Authentication -->
        <div id="project-face" class="tab-content">
            <a href="#" class="back-button" onclick="showTab(event, 'projects')">← Back to Projects</a>
            
            <div class="project-detail-header">
                <h1>Face Authentication System</h1>
                <p style="font-size: 1.2em; margin-top: 10px;">Banking Website Security</p>
                <div class="project-meta">
                    <div class="project-meta-item">
                        <span>📅</span>
                        <span>Aug 2023 - Oct 2023</span>
                    </div>
                    <div class="project-meta-item">
                        <span>🔒</span>
                        <span>Security System</span>
                    </div>
                    <div class="project-meta-item">
                        <span>🧑‍💻</span>
                        <span>Co-developed — team of 2</span>
                    </div>
                </div>
            </div>

            <div class="project-overview">
                <h2>Project Overview</h2>
                <p>
                    Built an end-to-end facial authentication system for a banking web application using Flask, OpenCV (LBPH), and MongoDB. Implemented secure user signup, face enrollment, and login with session management, confidence-based face verification, and server-side model persistence.
                </p>
                
                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Key Features</h3>
                <div class="features-grid">
                    <div class="feature-card">
                        <h3>👤 Face Recognition</h3>
                        <p>LBPH (Local Binary Patterns Histograms) algorithm for accurate facial recognition.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🔐 Secure Authentication</h3>
                        <p>Face recognition combined with password-based authentication.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📱 User Enrollment</h3>
                        <p>Simple enrollment process capturing multiple face angles for better recognition accuracy.</p>
                    </div>
                    <div class="feature-card">
                        <h3>💾 MongoDB Integration</h3>
                        <p>Secure storage of user credentials in MongoDB; trained face models persisted on the server.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🔄 Session Management</h3>
                        <p>Comprehensive session handling for secure user authentication and authorization.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📸 Real-time Capture</h3>
                        <p>Camera-based face capture for enrollment and authentication.</p>
                    </div>
                </div>

                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Technologies Used</h3>
                <div class="tech-stack-detail">
                    <span class="tech-badge-large">Python <small style="font-weight:400; opacity:0.85; font-size:0.78em">— core application logic</small></span>
                    <span class="tech-badge-large">Flask <small style="font-weight:400; opacity:0.85; font-size:0.78em">— web server &amp; API routes</small></span>
                    <span class="tech-badge-large">OpenCV <small style="font-weight:400; opacity:0.85; font-size:0.78em">— face detection &amp; image processing</small></span>
                    <span class="tech-badge-large">LBPH <small style="font-weight:400; opacity:0.85; font-size:0.78em">— face recognition algorithm</small></span>
                    <span class="tech-badge-large">MongoDB <small style="font-weight:400; opacity:0.85; font-size:0.78em">— stores face encodings</small></span>
                    <span class="tech-badge-large">Bootstrap <small style="font-weight:400; opacity:0.85; font-size:0.78em">— responsive UI layout</small></span>
                    <span class="tech-badge-large">JavaScript <small style="font-weight:400; opacity:0.85; font-size:0.78em">— frontend interactions</small></span>
                </div>
            </div>

            <div class="screenshots-section">
                <h2>Screenshots & Demo</h2>
                <div class="screenshots-grid">
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/fa_1.png') }}"  alt="Facial Authentication" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Face Authentication Login.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/fa_2.png') }}"  alt="Facial Authentication" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Live webcam-based face enrollment capturing multiple facial samples per user to train an LBPH recognition model.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/fa_3.png') }}"  alt="Facial Authentication" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Secure login flow combining password verification with live face capture for biometric authentication.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/fa_4.png') }}"  alt="Facial Authentication" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Successful biometric authentication with session-based access to a personalized banking dashboard and protected routes.</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Project 8: Portfolio Tracker -->
        <div id="project-portfolio" class="tab-content">
            <a href="#" class="back-button" onclick="showTab(event, 'projects')">← Back to Projects</a>
            
            <div class="project-detail-header">
                <h1>Investment Portfolio Tracker</h1>
                <div class="project-meta">
                    <div class="project-meta-item">
                        <span>📅</span>
                        <span>Feb 2023 - Apr 2023</span>
                    </div>
                    <div class="project-meta-item">
                        <span>💰</span>
                        <span>Finance Application</span>
                    </div>
                </div>
            </div>

            <div class="project-overview">
                <h2>Project Overview</h2>
                <p>
                    Built a Flask-based web application replicating a finance website with user sign-in/login, portfolio views, 
                    and investment calculators, focusing on realistic financial workflows.
                </p>
                <p>
                    Integrated the Polygon API to fetch real-time market data and implemented server-side logic for SIP and 
                    investment return calculations.
                </p>
                
                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Key Features</h3>
                <div class="features-grid">
                    <div class="feature-card">
                        <h3>🏦 Finance Website Replica</h3>
                        <p>Created a realistic finance website interface with portfolio views and financial workflows.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📈 Polygon API Integration</h3>
                        <p>Real-time stock market data fetching using Polygon API for live price updates.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🧮 Server-side SIP and investment return calculation logic</h3>
                        <p>Server-side SIP calculator and investment return calculators with comprehensive logic.</p>
                    </div>
                    <div class="feature-card">
                        <h3>👤 User Authentication</h3>
                        <p>Basic sign-in/login flow to demonstrate user access and navigation across portfolio features.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📊 Portfolio Views</h3>
                        <p>Comprehensive portfolio display with holdings, values, and investment tracking.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📱 Responsive UI</h3>
                        <p>Clean, professional interface built with Bootstrap for cross-device compatibility.</p>
                    </div>
                </div>

                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Technologies Used</h3>
                <div class="tech-stack-detail">
                    <span class="tech-badge-large">Python <small style="font-weight:400; opacity:0.85; font-size:0.78em">— server-side logic</small></span>
                    <span class="tech-badge-large">Flask <small style="font-weight:400; opacity:0.85; font-size:0.78em">— web framework</small></span>
                    <span class="tech-badge-large">Polygon API <small style="font-weight:400; opacity:0.85; font-size:0.78em">— real-time stock market data</small></span>
                    <span class="tech-badge-large">HTML/CSS <small style="font-weight:400; opacity:0.85; font-size:0.78em">— page structure &amp; styling</small></span>
                    <span class="tech-badge-large">Bootstrap <small style="font-weight:400; opacity:0.85; font-size:0.78em">— responsive layout</small></span>
                    <span class="tech-badge-large">JavaScript <small style="font-weight:400; opacity:0.85; font-size:0.78em">— interactive UI</small></span>
                </div>
            </div>

            <div class="screenshots-section">
                <h2>Screenshots & Demo</h2>
                <div class="screenshots-grid">
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/f_1.png') }}"  alt="Facial Authentication" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Main Portfolio Dashboard.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/f_2.png') }}"  alt="Facial Authentication" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">SIP Calculator with Server-Side Return Computation.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img  src="{{ url_for('static', filename='images/f_3.png') }}"  alt="Facial Authentication" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Stock Market Data Display Using Polygon API (Demo).</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Project 9: UCI PDF Temp Cleanup -->
        <div id="project-uci-pdf-cleanup" class="tab-content">
            <a href="#" class="back-button" onclick="showTab(event, 'projects')">← Back to Projects</a>

            <div class="project-detail-header">
                <h1>Automated PDF Temp Cleanup System</h1>
                <p style="font-size: 1.2em; margin-top: 10px;">Reusable across UCI, UAT &amp; PROD — AI-Powered Document Lifecycle Management</p>
                <div class="project-meta">
                    <div class="project-meta-item">
                        <span>📅</span>
                        <span>Jul 2026 - Present</span>
                    </div>
                    <div class="project-meta-item">
                        <span>🏢</span>
                        <span>UCI, UAT &amp; PROD @ Solartis LLC</span>
                    </div>
                    <div class="project-meta-item">
                        <span>👥</span>
                        <span>Internal Tool</span>
                    </div>
                </div>
            </div>

            <div class="project-overview">
                <h2>Project Overview</h2>
                <p>
                    Built to replace manual cleanup of temporary documents generated by a Solartis insurance platform.
                    Designed as a reusable system deployable across multiple environments — UCI, UAT, and PROD — each with
                    its own Flask REST API on a Linux VM. The API handles all file operations: scanning directories, extracting
                    dates from filenames, and deleting files older than the retention window. n8n orchestrates the full pipeline:
                    snapshot before, run cleanup, snapshot after, generate AI summary, send notifications.
                </p>
                <p>
                    Runs daily at 12 PM. After each run, a Qwen LLM (via LiteLLM) generates a 2–3 sentence professional
                    summary of what happened. Results are delivered as a rich Microsoft Teams Adaptive Card and a detailed
                    HTML email — both showing files before/after, disk freed, and a breakdown of files retained and deleted
                    by date. A cron watchdog separately monitors whether the cleanup ran and sends an alert email if it didn't.
                </p>

                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Key Features</h3>
                <div class="features-grid">
                    <div class="feature-card">
                        <h3>🗂️ Automated File Cleanup</h3>
                        <p>Scans MemoryPDF and SubMemoryPDF directories daily, deletes .pdf/.doc/.docx files older than the configured retention period based on dates in filenames.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🤖 AI-Generated Summaries</h3>
                        <p>Qwen LLM (via LiteLLM) produces a concise professional summary of each cleanup run, injected into both the email and Teams notification.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📨 Multi-Channel Notifications</h3>
                        <p>Microsoft Teams Adaptive Card and HTML email report after every run, showing AI summary, file counts, disk usage delta, and files retained/deleted by date.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🔌 REST API Architecture</h3>
                        <p>Flask API on the VM exposes /api/cleanup, /api/snapshot, /api/logs, and /health endpoints. n8n calls these via HTTP with API key authentication.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🛡️ Cron Watchdog</h3>
                        <p>A separate monitor script runs 5 minutes after the scheduled cleanup and sends an alert email if no evidence log is found for today's date.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🔐 Encrypted Secrets</h3>
                        <p>Sensitive credentials in .env are encrypted with AES-256-GCM. The app decrypts automatically on startup using a key file never committed to git.</p>
                    </div>
                </div>

                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Technologies Used</h3>
                <div class="tech-stack-detail">
                    <span class="tech-badge-large">Python <small style="font-weight:400; opacity:0.85; font-size:0.78em">— file ops, API logic &amp; encryption</small></span>
                    <span class="tech-badge-large">Flask <small style="font-weight:400; opacity:0.85; font-size:0.78em">— REST API endpoints</small></span>
                    <span class="tech-badge-large">n8n <small style="font-weight:400; opacity:0.85; font-size:0.78em">— orchestrates the full pipeline</small></span>
                    <span class="tech-badge-large">LiteLLM <small style="font-weight:400; opacity:0.85; font-size:0.78em">— routes requests to Qwen model</small></span>
                    <span class="tech-badge-large">Qwen (qwen3.6-27b-fp8) <small style="font-weight:400; opacity:0.85; font-size:0.78em">— generates AI cleanup summaries</small></span>
                    <span class="tech-badge-large">Microsoft Teams Adaptive Cards <small style="font-weight:400; opacity:0.85; font-size:0.78em">— rich card notification format</small></span>
                    <span class="tech-badge-large">Power Automate <small style="font-weight:400; opacity:0.85; font-size:0.78em">— bridges n8n to Teams channel</small></span>
                    <span class="tech-badge-large">Mailgun SMTP <small style="font-weight:400; opacity:0.85; font-size:0.78em">— sends HTML email reports</small></span>
                    <span class="tech-badge-large">systemd <small style="font-weight:400; opacity:0.85; font-size:0.78em">— runs Flask as a background service</small></span>
                    <span class="tech-badge-large">logrotate <small style="font-weight:400; opacity:0.85; font-size:0.78em">— manages &amp; rotates log files</small></span>
                    <span class="tech-badge-large">AES-256-GCM <small style="font-weight:400; opacity:0.85; font-size:0.78em">— encrypts .env credentials</small></span>
                    <span class="tech-badge-large">Linux (RHEL) <small style="font-weight:400; opacity:0.85; font-size:0.78em">— server OS for deployment</small></span>
                </div>
            </div>

            <div class="screenshots-section">
                <h2>Screenshots & Demo</h2>
                <div class="screenshots-grid">
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img src="{{ url_for('static', filename='images/pdf_cleanup_workflow.png') }}" alt="n8n Workflow" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Full n8n workflow showing all 11 nodes from Schedule Trigger to Teams/Email outputs.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img src="{{ url_for('static', filename='images/pdf_cleanup_email.png') }}" alt="Success Email Report" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Success email with AI Summary, Results table, Disk Usage table, and Files Retained/Deleted by Date.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img src="{{ url_for('static', filename='images/pdf_cleanup_teams.png') }}" alt="Teams Adaptive Card" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Microsoft Teams Adaptive Card with the same structured cleanup summary.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img src="{{ url_for('static', filename='images/pdf_cleanup_logs.png') }}" alt="Cleanup Evidence Logs" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">PuTTY terminal showing cleanup evidence log with deleted filenames.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img src="{{ url_for('static', filename='images/pdf_cleanup_ai_agent.png') }}" alt="n8n AI Agent Node" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">n8n AI Agent node prompt configuration using live data from previous nodes.</div>
                    </div>
                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img src="{{ url_for('static', filename='images/pdf_cleanup_qwen.png') }}" alt="Qwen LLM Output" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">LiteLLM Qwen model node showing input prompt and generated AI summary output.</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Project 10: Orchid MSI SharePoint Upload Automation -->
        <div id="project-orchid-msi" class="tab-content">
            <a href="#" class="back-button" onclick="showTab(event, 'projects')">← Back to Projects</a>

            <div class="project-detail-header">
                <h1>Orchid MSI SharePoint Upload Automation</h1>
                <p style="font-size: 1.2em; margin-top: 10px;">Fully automated daily document pipeline — from MySQL batch detection to verified SharePoint upload</p>
                <div class="project-meta">
                    <div class="project-meta-item">
                        <span>📅</span>
                        <span>May 2026 - Jul 2026</span>
                    </div>
                    <div class="project-meta-item">
                        <span>🏢</span>
                        <span>Production System @ Solartis LLC</span>
                    </div>
                    <div class="project-meta-item">
                        <span>👥</span>
                        <span>Internal Tool — Technology Team</span>
                    </div>
                </div>
            </div>

            <div class="project-overview">
                <h2>Project Overview</h2>
                <p>
                    Every working day, the Orchid MSI batch process generates a set of policy documents that must be verified
                    and uploaded to SharePoint before the team can proceed. Previously this was a fully manual workflow — someone
                    had to watch for the batch to complete, copy the files, check the PDFs, and upload them by hand. I built a
                    Flask-based automation system that handles the entire pipeline: a Kubernetes CronJob polls MySQL every
                    5 minutes for up to 4 hours waiting for the batch to reach COMPLETED status, then triggers file transfer,
                    PDF verification, and a SharePoint upload — sending a detailed HTML email to the team once done.
                </p>
                <p>
                    The system runs as two Kubernetes pods sharing an NFS volume — a persistent web app pod and a daily CronJob
                    pod. It includes a full admin dashboard with Azure AD SSO (Microsoft 365 login), role-based access control
                    (admin / user / viewer), a manual trigger button so any user can re-run the pipeline without kubectl access,
                    and 90-day screenshot retention as upload proof. A JavaScript bookmarklet handles the final SharePoint upload
                    step directly in the browser, automating folder detection and file deduplication.
                </p>

                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Key Features</h3>
                <div class="features-grid">
                    <div class="feature-card">
                        <h3>🔄 Automated Batch Detection</h3>
                        <p>Polls MySQL every 5 minutes for up to 4 hours waiting for COMPLETED status. Sends a fallback alert email with step-by-step manual instructions if the batch never completes.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📂 SFTP File Transfer</h3>
                        <p>Uses paramiko over SSH to pull today's policy ZIP files from the source server to NFS shared storage, making them available to the web app pod instantly.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🔖 SharePoint Bookmarklet</h3>
                        <p>A JavaScript bookmarklet injected into the SharePoint tab auto-detects the correct upload folder, deduplicates existing files, uploads in sequence, takes a proof screenshot, and reports back to the dashboard.</p>
                    </div>
                    <div class="feature-card">
                        <h3>✅ PDF Verification</h3>
                        <p>Checks that all expected PDFs are present and their counts match before any upload is triggered. Verification results are shown per-document on the dashboard and included in the email.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🔐 Azure AD SSO &amp; Role-Based Access</h3>
                        <p>Single sign-on via Microsoft 365 (MSAL). Three roles — admin, user, and viewer — control access to the manual trigger, admin panel, and read-only dashboard views.</p>
                    </div>
                    <div class="feature-card">
                        <h3>▶ Manual Trigger &amp; 90-Day Proof</h3>
                        <p>Admins and users can re-run the full file copy + verify + notify pipeline from the dashboard sidebar without any server access. Upload proof screenshots are retained for 90 days.</p>
                    </div>
                </div>

                <h3 style="color: #764ba2; margin-top: 30px; margin-bottom: 15px;">Technologies Used</h3>
                <div class="tech-stack-detail">
                    <span class="tech-badge-large">Python <small style="font-weight:400; opacity:0.85; font-size:0.78em">— DB polling, file ops &amp; email logic</small></span>
                    <span class="tech-badge-large">Flask <small style="font-weight:400; opacity:0.85; font-size:0.78em">— REST API endpoints &amp; admin dashboard</small></span>
                    <span class="tech-badge-large">JavaScript <small style="font-weight:400; opacity:0.85; font-size:0.78em">— SharePoint bookmarklet &amp; upload automation</small></span>
                    <span class="tech-badge-large">Bash <small style="font-weight:400; opacity:0.85; font-size:0.78em">— CronJob orchestration &amp; API calls</small></span>
                    <span class="tech-badge-large">paramiko <small style="font-weight:400; opacity:0.85; font-size:0.78em">— SSH/SFTP file transfer from source server</small></span>
                    <span class="tech-badge-large">MSAL <small style="font-weight:400; opacity:0.85; font-size:0.78em">— Azure AD SSO &amp; Microsoft token flow</small></span>
                    <span class="tech-badge-large">MySQL <small style="font-weight:400; opacity:0.85; font-size:0.78em">— batch COMPLETED status polling</small></span>
                    <span class="tech-badge-large">Kubernetes <small style="font-weight:400; opacity:0.85; font-size:0.78em">— two-pod deployment with NFS shared volume</small></span>
                    <span class="tech-badge-large">AES-256-GCM <small style="font-weight:400; opacity:0.85; font-size:0.78em">— credential encryption at rest</small></span>
                </div>
            </div>

            <div class="screenshots-section">
                <h2>Screenshots &amp; Demo</h2>
                <div class="screenshots-grid">

                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img src="{{ url_for('static', filename='images/msi_email.png') }}" alt="Success notification email" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Success email — sent to the team once PDFs are verified and upload is complete, with a direct link to the dashboard</div>
                    </div>

                    <div class="screenshot-item">
                        <img src="{{ url_for('static', filename='images/msi_before_file_not_generated.png') }}" alt="Dashboard before files are generated" style="width:100%; border-radius:14px;">
                        <div class="screenshot-caption">Dashboard state while waiting for the batch to reach COMPLETED — polling is active</div>
                    </div>

                    <div class="screenshot-item">
                        <img src="{{ url_for('static', filename='images/msi_files_generated.png') }}" alt="Dashboard after files are generated" style="width:100%; border-radius:14px;">
                        <div class="screenshot-caption">Files detected and copied — PDF verification results shown per document</div>
                    </div>

                    <div class="screenshot-item">
                        <img src="{{ url_for('static', filename='images/msi_setup_bookmarklet.png') }}" alt="Bookmarklet setup dialog" style="width:100%; border-radius:14px;">
                        <div class="screenshot-caption">One-time bookmarklet setup — drag the button into Chrome bookmarks bar to enable SharePoint upload</div>
                    </div>

                    <div class="screenshot-item">
                        <img src="{{ url_for('static', filename='images/msi_route_to_sharepoint.png') }}" alt="SharePoint routing dialog" style="width:100%; border-radius:14px;">
                        <div class="screenshot-caption">Upload dialog opens SharePoint in a new tab and prompts the user to click the bookmarklet</div>
                    </div>

                    <div class="screenshot-item">
                        <img src="{{ url_for('static', filename='images/msi_after_triggering_bookmarklet.png') }}" alt="Bookmarklet running upload" style="width:100%; border-radius:14px;">
                        <div class="screenshot-caption">Bookmarklet in action — status overlay shows each file being checked and uploaded in real time</div>
                    </div>

                    <div class="screenshot-item" style="grid-column: 1 / -1;">
                        <img src="{{ url_for('static', filename='images/msi_app_after_successful_upload.png') }}" alt="Dashboard after successful upload" style="width:100%; max-width: 1200px; display: block; margin: 0 auto; border-radius:14px;">
                        <div class="screenshot-caption">Dashboard after a clean upload — green success banner, file count confirmed, local folder deleted automatically</div>
                    </div>

                    <div class="screenshot-item">
                        <img src="{{ url_for('static', filename='images/msi_file_uploaded_and_scrrenshot_taken.png') }}" alt="File uploaded and screenshot captured" style="width:100%; border-radius:14px;">
                        <div class="screenshot-caption">SharePoint folder after upload — proof screenshot captured automatically by the bookmarklet</div>
                    </div>

                    <div class="screenshot-item">
                        <img src="{{ url_for('static', filename='images/msi_screenshot_tab_before_upload_to_sharepoint.png') }}" alt="Screenshots tab" style="width:100%; border-radius:14px;">
                        <div class="screenshot-caption">Screenshots tab — proof screenshots listed by date, retained for 90 days</div>
                    </div>

                    <div class="screenshot-item">
                        <img src="{{ url_for('static', filename='images/msi_opening_the_screenshot.png') }}" alt="Viewing a proof screenshot" style="width:100%; border-radius:14px;">
                        <div class="screenshot-caption">Proof screenshot preview — full-resolution view of a completed upload for audit or compliance</div>
                    </div>

                    <div class="screenshot-item">
                        <img src="{{ url_for('static', filename='images/msi_newly_scrrenshot.png') }}" alt="Newly captured screenshot" style="width:100%; border-radius:14px;">
                        <div class="screenshot-caption">Freshly captured screenshot appearing in the gallery immediately after upload completes</div>
                    </div>

                    <div class="screenshot-item">
                        <img src="{{ url_for('static', filename='images/msi_admin_panel_user_section.png') }}" alt="Admin panel — user management" style="width:100%; border-radius:14px;">
                        <div class="screenshot-caption">Admin panel — manage team members and assign roles (admin / user / viewer)</div>
                    </div>

                    <div class="screenshot-item">
                        <img src="{{ url_for('static', filename='images/msi_admin_panel_add_recipient.png') }}" alt="Admin panel — email recipients" style="width:100%; border-radius:14px;">
                        <div class="screenshot-caption">Admin panel — configure email recipients for success and fallback notifications</div>
                    </div>

                </div>
            </div>
        </div>

        <!-- Contact Tab -->
        <div id="contact" class="tab-content">
            <div class="section">
                <h2>Get In Touch</h2>
                <p style="font-size: 1.1em; color: #555; margin-bottom: 30px;">
                    I'm always open to discussing new projects, creative ideas, or opportunities to be part of your vision. 
                    Feel free to reach out through any of the channels below!
                </p>
                
                <div class="contact-grid">
                    <div class="contact-card">
                        <div class="icon">📧</div>
                        <h3>Email</h3>
                        <p><a href="mailto:aswinthmani10@gmail.com">aswinthmani10@gmail.com</a></p>
                    </div>
                    
                    <div class="contact-card">
                        <div class="icon">📱</div>
                        <h3>Phone</h3>
                        <p><a href="tel:7358348418">+91 735 834 8418</a></p>
                    </div>
                    
                    <div class="contact-card">
                        <div class="icon">💼</div>
                        <h3>LinkedIn</h3>
                        <p><a href="https://linkedin.com/in/aswinthmani-v-ab6852240" target="_blank">aswinthmani-v</a></p>
                    </div>
                    
                    <div class="contact-card">
                        <div class="icon">🐙</div>
                        <h3>GitHub</h3>
                        <p><a href="https://github.com/Aswinthmani2003" target="_blank">Aswinthmani2003</a></p>
                    </div>
                    
                    <div class="contact-card">
                        <div class="icon">📍</div>
                        <h3>Location</h3>
                        <p>Mylapore, Chennai<br>Tamil Nadu, India</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2025 Aswinthmani V. All rights reserved.</p>
        <p style="margin-top: 10px; opacity: 0.8;">Built with Flask & passion for AI</p>
    </footer>

    <script>
        function showTab(event, tabName) {
            // Prevent default link behavior
            if (event) {
                event.preventDefault();
            }
            
            // Hide all tab content
            const tabContents = document.getElementsByClassName('tab-content');
            for (let i = 0; i < tabContents.length; i++) {
                tabContents[i].classList.remove('active');
            }
            
            // Remove active class from all nav links
            const navLinks = document.getElementsByClassName('nav-link');
            for (let i = 0; i < navLinks.length; i++) {
                navLinks[i].classList.remove('active');
            }
            
            // Show the current tab
            document.getElementById(tabName).classList.add('active');
            
            // Add active class to the appropriate nav link
            if (tabName === 'home') {
    document.querySelector('a[onclick*="home"]').classList.add('active');
} else if (tabName === 'about') {
    document.querySelector('a[onclick*="about"]').classList.add('active');
} else if (tabName === 'education') {
    document.querySelector('a[onclick*="education"]').classList.add('active');
} else if (tabName === 'experience') {
    document.querySelector('a[onclick*="experience"]').classList.add('active');
} else if (tabName === 'skills') {
    document.querySelector('a[onclick*="skills"]').classList.add('active');
} else if (tabName === 'projects' || tabName.startsWith('project-')) {
    document.querySelector('a[onclick*="projects"]').classList.add('active');
} else if (tabName === 'contact') {
    document.querySelector('a[onclick*="contact"]').classList.add('active');
}

            
            // Close mobile menu after selection
            document.getElementById('navLinks').classList.remove('active');
            
            // Scroll to top
            window.scrollTo({top: 0, behavior: 'smooth'});
        }
        
        function toggleMobileMenu() {
            document.getElementById('navLinks').classList.toggle('active');
        }
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            const nav = document.getElementById('navLinks');
            const toggle = document.querySelector('.mobile-menu-toggle');

            if (!nav.contains(event.target) && !toggle.contains(event.target)) {
                nav.classList.remove('active');
            }
        });

        /* ============================================================
           INTERACTION LAYER
           ============================================================ */
        (function () {
            const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

            /* ---------- 1. Scroll progress bar ---------- */
            const bar = document.getElementById('scrollProgress');
            function updateProgress() {
                const max = document.documentElement.scrollHeight - window.innerHeight;
                const pct = max > 0 ? (window.scrollY / max) * 100 : 0;
                bar.style.width = pct + '%';
            }
            window.addEventListener('scroll', updateProgress, { passive: true });
            window.addEventListener('resize', updateProgress);
            updateProgress();

            /* ---------- 2. Cursor glow (smoothed) ---------- */
            const glow = document.getElementById('cursorGlow');
            let gx = window.innerWidth / 2, gy = window.innerHeight / 2, tx = gx, ty = gy;
            if (!reduced && window.matchMedia('(hover:hover)').matches) {
                window.addEventListener('mousemove', function (e) {
                    tx = e.clientX; ty = e.clientY;
                    glow.classList.add('on');
                }, { passive: true });
                (function loop() {
                    gx += (tx - gx) * 0.12;
                    gy += (ty - gy) * 0.12;
                    glow.style.transform = 'translate(' + gx + 'px,' + gy + 'px) translate(-50%,-50%)';
                    requestAnimationFrame(loop);
                })();
            }

            /* ---------- 3. Scroll reveal ---------- */
            const REVEAL_SEL = [
                '.hero', '.section', '.project-card', '.skill-card', '.feature-card',
                '.interest-card', '.contact-card', '.screenshot-item', '.education-card',
                '.project-overview', '.screenshots-section', '.project-detail-header'
            ].join(',');

            const io = new IntersectionObserver(function (entries) {
                entries.forEach(function (en) {
                    if (en.isIntersecting) {
                        en.target.classList.add('is-visible');
                        io.unobserve(en.target);
                    }
                });
            }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

            function initReveal(scope) {
                const els = (scope || document).querySelectorAll(REVEAL_SEL);
                els.forEach(function (el, i) {
                    el.classList.add('reveal-target');
                    el.classList.remove('is-visible');
                    el.style.transitionDelay = Math.min(i * 50, 340) + 'ms';
                    io.observe(el);
                });
            }
            initReveal();

            /* Re-run reveal + interactions whenever a tab changes */
            const originalShowTab = window.showTab;
            window.showTab = function (event, tabName) {
                originalShowTab(event, tabName);
                const panel = document.getElementById(tabName);
                if (panel) {
                    initReveal(panel);
                    wire(panel);
                }
                updateProgress();
            };

            /* ---------- 4. Pointer spotlight + 3D tilt ---------- */
            const SPOT_SEL = '.skill-card,.feature-card,.contact-card,.project-card,.interest-card';
            const TILT_SEL = '.project-card,.screenshot-item';

            function wire(scope) {
                const root = scope || document;

                root.querySelectorAll(SPOT_SEL).forEach(function (el) {
                    if (el.dataset.spot) return;
                    el.dataset.spot = '1';
                    el.addEventListener('mousemove', function (e) {
                        const r = el.getBoundingClientRect();
                        el.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100) + '%');
                        el.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100) + '%');
                    }, { passive: true });
                });

                if (reduced) return;
                root.querySelectorAll(TILT_SEL).forEach(function (el) {
                    if (el.dataset.tilt) return;
                    el.dataset.tilt = '1';
                    const MAX = el.classList.contains('project-card') ? 5 : 3;
                    el.addEventListener('mousemove', function (e) {
                        const r = el.getBoundingClientRect();
                        const px = (e.clientX - r.left) / r.width;
                        const py = (e.clientY - r.top) / r.height;
                        el.style.transform =
                            'perspective(1000px) rotateX(' + ((py - 0.5) * -MAX).toFixed(2) + 'deg) ' +
                            'rotateY(' + ((px - 0.5) * MAX).toFixed(2) + 'deg) translateY(-6px)';
                    }, { passive: true });
                    el.addEventListener('mouseleave', function () { el.style.transform = ''; });
                });
            }
            wire();

            /* ---------- 5. Magnetic buttons ---------- */
            if (!reduced) {
                document.querySelectorAll('.contact-btn,.cert-btn').forEach(function (btn) {
                    btn.addEventListener('mousemove', function (e) {
                        const r = btn.getBoundingClientRect();
                        const dx = (e.clientX - (r.left + r.width / 2)) / r.width;
                        const dy = (e.clientY - (r.top + r.height / 2)) / r.height;
                        btn.style.transform = 'translate(' + (dx * 9).toFixed(1) + 'px,' + (dy * 9 - 3).toFixed(1) + 'px)';
                    }, { passive: true });
                    btn.addEventListener('mouseleave', function () { btn.style.transform = ''; });
                });
            }

            /* ---------- 6. In-page PDF viewer ----------
               The anchors keep target="_blank" as a no-JS fallback; we
               intercept the click and render the PDF in an iframe instead. */
            const modal   = document.getElementById('pdfModal');
            const frame   = document.getElementById('pdfFrame');
            const mTitle  = document.getElementById('pdfModalTitle');
            const mNewTab = document.getElementById('pdfOpenNew');

            function openPdf(url, title) {
                frame.src = url;
                mTitle.textContent = title;
                mNewTab.href = url;
                modal.classList.add('open');
                document.body.style.overflow = 'hidden';
            }
            function closePdf() {
                modal.classList.remove('open');
                document.body.style.overflow = '';
                setTimeout(function () { frame.src = 'about:blank'; }, 320);
            }

            document.querySelectorAll('.cert-btn').forEach(function (btn) {
                btn.addEventListener('click', function (e) {
                    e.preventDefault();
                    const card = btn.closest('.skill-card');
                    const head = card ? card.querySelector('h3') : null;
                    openPdf(btn.getAttribute('href'), head ? head.textContent.trim() : 'Certificate');
                });
            });
            modal.querySelectorAll('[data-close]').forEach(function (el) {
                el.addEventListener('click', closePdf);
            });
            document.addEventListener('keydown', function (e) {
                if (e.key === 'Escape' && modal.classList.contains('open')) closePdf();
            });

            /* ---------- 7. Screenshot lightbox ----------
               Tiles are uniformly sized, so this is how you read the detail.
               Delegated from document so it covers every tab without rewiring. */
            const lb     = document.getElementById('imgLightbox');
            const lbImg  = document.getElementById('imgLightboxImg');
            const lbCap  = document.getElementById('imgLightboxCap');

            function openLightbox(src, caption, alt) {
                lbImg.src = src;
                lbImg.alt = alt || caption || 'Screenshot';
                lbCap.textContent = caption || '';
                lb.classList.add('open');
                document.body.style.overflow = 'hidden';
            }
            function closeLightbox() {
                lb.classList.remove('open');
                document.body.style.overflow = '';
                setTimeout(function () { lbImg.src = ''; }, 320);
            }

            document.addEventListener('click', function (e) {
                const img = e.target.closest ? e.target.closest('.screenshot-item img') : null;
                if (!img) return;
                const item = img.closest('.screenshot-item');
                const cap  = item ? item.querySelector('.screenshot-caption') : null;
                openLightbox(img.currentSrc || img.src, cap ? cap.textContent.trim() : '', img.alt);
            });
            lb.querySelectorAll('[data-imgclose]').forEach(function (el) {
                el.addEventListener('click', closeLightbox);
            });
            document.addEventListener('keydown', function (e) {
                if (e.key === 'Escape' && lb.classList.contains('open')) closeLightbox();
            });

            /* ---------- 8. Hero typing effect ---------- */
            const h1 = document.querySelector('.hero h1');
            if (h1 && !reduced) {
                const full = h1.textContent.trim();
                h1.textContent = '';
                const caret = document.createElement('span');
                caret.className = 'caret';
                caret.textContent = '_';
                h1.appendChild(caret);
                let i = 0;
                (function type() {
                    if (i <= full.length) {
                        caret.insertAdjacentText('beforebegin', full.charAt(i - 1) || '');
                        i++;
                        setTimeout(type, 68);
                    } else {
                        setTimeout(function () { caret.remove(); }, 1600);
                    }
                })();
            }
        })();
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)
