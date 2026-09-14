import os
from PIL import Image
import streamlit as strlit

# Page configuration
strlit.set_page_config(
    page_title="ByeByeBites - Natural Mosquito Protection",
    page_icon="🦟",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom Styling with Google Fonts & Forest Green Theme
strlit.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #F8F9FA;
    }

    h1, h2, h3, h4, h5, h6, .hero-title {
        font-family: 'Outfit', sans-serif !important;
    }

    .hero-container {
        background: linear-gradient(135deg, #1E4D2B 0%, #2C5E3B 100%);
        padding: 45px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 10px;
        letter-spacing: 1px;
        color: white !important;
    }
    .hero-subtitle {
        font-size: 1.3rem;
        font-weight: 300;
        margin-bottom: 20px;
        opacity: 0.9;
        color: white !important;
    }
    .section-header {
        color: #ffffff;
        background-color: #1E4D2B;
        padding: 12px 20px;
        border-radius: 8px;
        margin-top: 35px;
        margin-bottom: 20px;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    .statement-card {
        background: #1E4D2B;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        text-align: center;
        height: 100%;
        color: white !important;
        border-left: 6px solid #2C5E3B;
    }
    .statement-card h3 {
        color: #ffffff !important;
        margin-bottom: 15px;
    }
    .statement-card p {
        color: #f1f1f1 !important;
        font-size: 1.05rem;
        line-height: 1.5;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        text-align: center;
        height: 100%;
        border-top: 4px solid #1E4D2B;
    }
    .team-card {
        background: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 20px;
        border-top: 3px solid #1E4D2B;
    }
    .badge {
        background-color: #E8F5E9;
        color: #1E4D2B;
        padding: 6px 12px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
        margin: 4px;
    }
    .contact-footer {
        background-color: #1E4D2B;
        color: white;
        padding: 30px;
        border-radius: 15px;
        margin-top: 40px;
        text-align: center;
    }
    .tino-footer {
        background: linear-gradient(135deg, #111827 0%, #1F2937 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        margin-top: 30px;
        text-align: center;
        border: 2px solid #1E4D2B;
    }
    .qr-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        text-align: center;
        border-top: 4px solid #25D366;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .whatsapp-btn {
        background-color: #25D366;
        color: white;
        padding: 10px 20px;
        border-radius: 30px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        margin-top: 10px;
        box-shadow: 0 4px 10px rgba(37, 211, 102, 0.3);
    }
    .whatsapp-btn:hover {
        background-color: #20ba5a;
        color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Image Directory Path pointing to GitHub 'assets' folder
IMAGE_DIR = "assets"


def load_image(filename):
  path = os.path.join(IMAGE_DIR, filename)
  if os.path.exists(path):
    return Image.open(path)
  return None


# --- HERO SECTION ---
strlit.markdown(
    """
    <div class="hero-container">
        <div class="hero-title">BYEBYE BITES</div>
        <div class="hero-subtitle">Eucalyptus Oil Mosquito Repellent Lotion — Natural Protection You Can Trust</div>
        <p style="font-style: italic; font-size: 1.1rem; color: white;">“Don't let mosquitoes crash the braai!!!”</p>
    </div>
""",
    unsafe_allow_html=True,
)

# --- VISION & MISSION ---
col_v, col_m = strlit.columns(2)
with col_v:
  strlit.markdown(
      """
        <div class="statement-card">
            <h3>Vision Statement</h3>
            <p>“To be the trusted, natural choice that keeps every family protected from mosquito bites—safely, effectively, and sustainably.”</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

with col_m:
  strlit.markdown(
      """
        <div class="statement-card">
            <h3>Mission Statement</h3>
            <p>“ByeByeBites exists to provide safe, plant-based mosquito protection through high-quality eucalyptus-oil lotion that is gentle on skin, kind to the environment, and accessible to all.”</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

strlit.markdown("<br>", unsafe_allow_html=True)

# --- PRODUCT SHOWCASE & FLYER ---
strlit.markdown(
    '<div class="section-header">🌿 Product & Flyer Overview</div>',
    unsafe_allow_html=True,
)
col_flyer1, col_flyer2 = strlit.columns(2)

with col_flyer1:
  flyer_img = load_image("Better_Poster_Flyer.jpeg")
  if flyer_img:
    strlit.image(
        flyer_img,
        caption="ByeByeBites Promotional Flyer",
        use_container_width=True,
    )
  else:
    strlit.info("Flyer image placeholder (Better_Poster_Flyer.jpeg)")

with col_flyer2:
  poster_img = load_image("Poster_Flyer.jpeg")
  if poster_img:
    strlit.image(
        poster_img,
        caption="ByeByeBites Brand Variations",
        use_container_width=True,
    )
  else:
    strlit.info("Poster image placeholder (Poster_Flyer.jpeg)")

# --- PRODUCT PRICING & SIZES ---
strlit.markdown(
    '<div class="section-header">📦 Available Sizes & Pricing</div>',
    unsafe_allow_html=True,
)

pricing_col1, pricing_col2, pricing_col3, pricing_col4 = strlit.columns(4)

with pricing_col1:
  strlit.markdown(
      """
        <div class="card">
            <h4>60 ml</h4>
            <p style="color: #666;">Travel Size</p>
            <h3 style="color: #1E4D2B;">R49.99</h3>
            <span class="badge">Compact & Handy</span>
        </div>
        """,
      unsafe_allow_html=True,
  )

with pricing_col2:
  strlit.markdown(
      """
        <div class="card">
            <h4>120 ml</h4>
            <p style="color: #666;">Everyday Protection</p>
            <h3 style="color: #1E4D2B;">R79.99</h3>
            <span class="badge">Most Popular</span>
        </div>
        """,
      unsafe_allow_html=True,
  )

with pricing_col3:
  strlit.markdown(
      """
        <div class="card">
            <h4>250 ml</h4>
            <p style="color: #666;">Family Size</p>
            <h3 style="color: #1E4D2B;">R129.99</h3>
            <span class="badge">Great Value</span>
        </div>
        """,
      unsafe_allow_html=True,
  )

with pricing_col4:
  strlit.markdown(
      """
        <div class="card">
            <h4>500 ml</h4>
            <p style="color: #666;">Value Size</p>
            <h3 style="color: #1E4D2B;">R199.99</h3>
            <span class="badge">Maximum Savings</span>
        </div>
        """,
      unsafe_allow_html=True,
  )

strlit.markdown("<br>", unsafe_allow_html=True)

# --- LEADERSHIP & TEAM ---
strlit.markdown(
    '<div class="section-header">👥 Meet Our Management Team</div>',
    unsafe_allow_html=True,
)

team_members = [
    {
        "name": "Nemudzivhadi T",
        "role": "Chief Executive Officer",
        "img": "Nemudzivhadi T _ Chief Executive Officer.jpeg",
    },
    {
        "name": "Netshitangani A",
        "role": "Operations Director",
        "img": "Netshitangani A _ Operations Director.jpeg",
    },
    {
        "name": "Mudimeli N",
        "role": "Finance Manager",
        "img": "Mudimeli N _ Finance Manager.jpeg",
    },
    {
        "name": "Ratshilumela L",
        "role": "Marketing Manager",
        "img": "Marketing Manager _ Ratshilumela L.jpeg",
    },
    {
        "name": "Dikotla J",
        "role": "Production Manager",
        "img": "Dikotla J _ Production Manager.jpeg",
    },
    {
        "name": "Miss Elethu",
        "role": "Shop Manager",
        "img": "Miss Elethu _ Shop Manager.jpeg",
    },
    {
        "name": "Nedombeni Mufunwa",
        "role": "Stock and Inventory Manager",
        "img": "Nedombeni Mufunwa _ Stock and Inventory Manager.jpeg",
    },
    {
        "name": "Thovhakale R",
        "role": "Customer Care Assistant",
        "img": "Thovhakale R _ Custommer Care Assistant.jpeg",
    },
    {
        "name": "Ravele R",
        "role": "Cashier 1",
        "img": "Cashier 1 _ Ravele R.jpeg",
    },
    {
        "name": "Marvellous M",
        "role": "Cashier 2",
        "img": "Cashier 2 _ Marvellous M.jpeg",
    },
]

# Display team members in a 4-column grid
cols_per_row = 4
for i in range(0, len(team_members), cols_per_row):
  row_cols = strlit.columns(cols_per_row)
  for j in range(cols_per_row):
    if i + j < len(team_members):
      member = team_members[i + j]
      with row_cols[j]:
        strlit.markdown('<div class="team-card">', unsafe_allow_html=True)
        img = load_image(member["img"])
        if img:
          strlit.image(img, use_container_width=True)
        else:
          strlit.text("Photo unavailable")
        strlit.markdown(
            f"**{member['name']}**<br><span"
            f' style="color: #1E4D2B; font-weight: 500; font-size:'
            f' 0.9rem;">{member["role"]}</span>',
            unsafe_allow_html=True,
        )
        strlit.markdown("</div>", unsafe_allow_html=True)

# --- CONTACT & LOCATION FOOTER ---
strlit.markdown(
    """
    <div class="contact-footer">
        <h2 style="margin-bottom: 15px;">Get In Touch With Us</h2>
        <p style="font-size: 1.05rem; margin-bottom: 8px;">
            📧 <b>Email:</b> byebyebite10@gmail.com &nbsp;&nbsp;|&nbsp;&nbsp; 
            📞 <b>Phone:</b> 071 618 0651 &nbsp;&nbsp;|&nbsp;&nbsp; 
            💬 <b>WhatsApp:</b> 060 137 1144
        </p>
        <p style="font-size: 1rem; margin-bottom: 15px;">
            📍 <b>Location:</b> Thohoyandou, University of Venda Main Gate
        </p>
        <hr style="border-color: rgba(255,255,255,0.2); margin: 15px auto; width: 80%;">
        <p style="font-size: 0.85rem; opacity: 0.8;">© 2026 ByeByeBites. All rights reserved. Natural protection you can trust.</p>
    </div>
""",
    unsafe_allow_html=True,
)

# --- TINO LABS / DEVELOPER PROMOTION & QR CODE FOOTER ---
strlit.markdown("<br>", unsafe_allow_html=True)

tino_col1, tino_col2 = strlit.columns([1.3, 1])

with tino_col1:
  strlit.markdown(
      """
        <div class="tino-footer" style="text-align: left; height: 100%; display: flex; flex-direction: column; justify-content: center; padding: 25px; margin-top: 0;">
            <h3 style="color: #25D366; margin-bottom: 10px; font-size: 1.4rem;">Want a website or data solution like this?</h3>
            <p style="font-size: 0.95rem; color: #D1D5DB; margin-bottom: 15px; line-height: 1.5;">
                Partner with <b>Tino Labs</b> for custom web applications, professional branding, and automated data workflows tailored to your business.
            </p>
            <p style="font-size: 0.95rem; margin-bottom: 15px;">
                📞 <b>Direct:</b> <a href="https://wa.me/27812678907" style="color: #25D366; text-decoration: none; font-weight: 700;">+27 81 267 8907</a>
            </p>
            <div>
                <a href="https://wa.me/27812678907?text=Hi%20Tino,%20I%20saw%20your%20work%20on%20the%20ByeByeBites%20website%20and%20I'd%20like%20to%20discuss%20a%20project!" target="_blank" class="whatsapp-btn">💬 Chat with Tino Labs</a>
            </div>
        </div>
        """,
      unsafe_allow_html=True,
  )

with tino_col2:
  strlit.markdown(
      """
        <div class="qr-card">
            <h4 style="color: #111827; margin-bottom: 10px; font-size: 1.2rem; font-family: 'Outfit', sans-serif;">Scan to Connect</h4>
        """,
      unsafe_allow_html=True,
  )
  qr_img = load_image("Screenshot_20260914_222234_WhatsApp.jpg.jpeg")
  if qr_img:
    strlit.image(qr_img, width=170)
  else:
    strlit.info("WhatsApp QR Code placeholder")
  strlit.markdown(
      '<p style="font-size: 0.85rem; color: #4B5563; margin-top: 10px;'
      ' font-weight: 500;">WhatsApp: +27 81 267 8907</p></div>',
      unsafe_allow_html=True,
  )
