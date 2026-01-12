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
</head>
<body>
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
                <p class="title">AI & Automation Engineer (Finance-Focused)</p>
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
        <li>Strong backend foundation using Python, Flask/FastAPI, MongoDB, and REST APIs</li>
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
                            Hello! I'm Aswinthmani V, an AI & Data Science enthusiast currently pursuing my B.Tech in Artificial 
                            Intelligence and Data Analytics at Sri Ramachandra Institute of Higher Education and Research, Chennai.
                        </p>
                        <p>
                            My journey in technology is driven by curiosity and a passion for automation. I believe in learning by 
                            building, which is why I've worked on diverse projects ranging from facial authentication systems to 
                            AI-powered chatbots for financial services.
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
                        <h3>☁️ AWS ML Foundations</h3>
                        <p style="color: #555; margin-top: 10px;">
                            Comprehensive understanding of machine learning fundamentals and AWS ML services
                        </p>
                    </div>
                    <div class="skill-card">
                        <h3>🤖 Generative AI</h3>
                        <p style="color: #555; margin-top: 10px;">
                            Advanced concepts in generative AI and large language models
                        </p>
                    </div>
                    <div class="skill-card">
                        <h3>☁️ Oracle AI Vector Search Certified Professional</h3>
                        <p style="color: #555; margin-top: 10px;">
                            Expertise in vector databases, similarity search, embeddings, and AI-powered semantic retrieval using Oracle AI Vector Search
                        </p>
                    </div>
                    <div class="skill-card">
                        <h3>☁️ Oracle Cloud Infrastructure (OCI) 2025 – AI Foundations Associate</h3>
                        <p style="color: #555; margin-top: 10px;">
                            Strong foundation in AI concepts, OCI services, model lifecycle, and enterprise AI deployment fundamentals
                        </p>
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
                <h3>AIML / Automation Intern — App Synergies</h3>
                <span class="project-date">Feb 2025 – Jul 2025</span>
            </div>
            <p>
                Worked on production-grade automation and AI systems involving WhatsApp Cloud API, CRM workflows,
                and real-time dashboards for business operations.
            </p>
            <ul style="margin-top: 10px; color: #555;">
                <li>Developed an AI-driven system for sales teams, automating lead qualification, meeting scheduling, and follow-ups, with integrated time zone intelligence and regional routing.</li>
                <li>Built an open-source proposal generator that automates professional proposal creation with dynamic templates, integrating Google Cloud for deployment and document generation.</li>
                <li>Worked with real client data, maintained automation pipelines, implemented real-time monitoring, and handled production constraints.</li>
            </ul>
        </div>

        <div class="project-card">
            <div class="project-header">
                <h3>Full Stack Developer Intern  — LIA Infraservices</h3>
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
                            <li>SQL</li>
                            <li>JavaScript</li>
                            <li>HTML</li>
                            <li>CSS</li>
                        </ul>
                    </div>
                    <div class="skill-card">
                        <h3>🛠️ Frameworks & Libraries</h3>
                        <ul>
                            <li>FastAPI</li>
                            <li>Flask</li>
                            <li>Streamlit</li>
                            <li>Express.js</li> 
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
                            <li>Manychats</li>
                            <li>Retell AI</li>
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
                            <li>Automation</li>
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
                            <li>AWS Services</li>
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
                        <span class="project-date">Dec 2025 - Present</span>
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
                        <span>Dec 2025 - Present</span>
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
                    <span class="tech-badge-large">WhatsApp Cloud API</span>
                    <span class="tech-badge-large">Python</span>
                    <span class="tech-badge-large">Flask</span>
                    <span class="tech-badge-large">MongoDB</span>
                    <span class="tech-badge-large">JavaScript</span>
                    <span class="tech-badge-large">Make.com</span>
                    <span class="tech-badge-large">GPT-4</span>
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
                    <span class="tech-badge-large">Python</span>
                    <span class="tech-badge-large">Google Cloud Platform</span>
                    <span class="tech-badge-large">Document Automation</span>
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
                    <span class="tech-badge-large">Retell AI</span>
                    <span class="tech-badge-large">Make.com</span>
                    <span class="tech-badge-large">Google Calendar</span>
                    <span class="tech-badge-large">Microsoft Teams</span>
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
                    <span class="tech-badge-large">WhatsApp Cloud API</span>
                    <span class="tech-badge-large">Meta WhatsApp Manager</span>
                    <span class="tech-badge-large">Zoho CRM</span>
                    <span class="tech-badge-large">Make.com</span>
                    <span class="tech-badge-large">REST APIs & Webhooks</span>
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
                    <span class="tech-badge-large">🐍 Backend: Flask (Python)</span>
                    <span class="tech-badge-large">🧠 LLM Inference: Groq API · Llama 3.3</span>
                    <span class="tech-badge-large">🌐 Frontend: HTML, CSS, Vanilla JavaScript</span>
                    <span class="tech-badge-large">📊 Visualization: Chart.js</span>
                    <span class="tech-badge-large">📄 Reports: ReportLab (PDF generation)</span>
                </div>
            </div>

            <div class="screenshots-section">
                <h2>Screenshots & Demo</h2>
                <div class="screenshots-grid">
                    <<div class="screenshot-item" style="grid-column: 1 / -1;">
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
                    <span class="tech-badge-large">Python</span>
                    <span class="tech-badge-large">Selenium</span>
                    <span class="tech-badge-large">TextBlob</span>
                    <span class="tech-badge-large">NLP</span>
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
                </div>
            </div>

            <div class="project-overview">
                <h2>Project Overview</h2>
                <p>
                    Built an end-to-end facial authentication system for a banking web application using Flask, OpenCV (LBPH), and MongoDB. Implemented secure user signup, face enrollment, and login with session management, confidence-based face verification, and server-side model persistence.
                </p>
                
                <h3 style="color
                
                : #764ba2; margin-top: 30px; margin-bottom: 15px;">Key Features</h3>
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
                    <span class="tech-badge-large">Python</span>
                    <span class="tech-badge-large">Flask</span>
                    <span class="tech-badge-large">OpenCV</span>
                    <span class="tech-badge-large">LBPH</span>
                    <span class="tech-badge-large">MongoDB</span>
                    <span class="tech-badge-large">Bootstrap</span>
                    <span class="tech-badge-large">JavaScript</span>
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
                    <span class="tech-badge-large">Python</span>
                    <span class="tech-badge-large">Flask</span>
                    <span class="tech-badge-large">Polygon API</span>
                    <span class="tech-badge-large">HTML/CSS</span>
                    <span class="tech-badge-large">Bootstrap</span>
                    <span class="tech-badge-large">JavaScript</span>
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
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)
