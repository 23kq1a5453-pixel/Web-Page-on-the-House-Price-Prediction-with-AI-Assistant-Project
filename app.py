import streamlit as st

st.set_page_config(page_title="Property Planning Dashboard", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #eaf3ff 0%, #f8fbff 100%);
    }
    .main-title {
        font-size: 2.3rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1rem;
        color: #475569;
        margin-bottom: 1rem;
    }
    .info-box {
        background: #ffffff;
        border: 1px solid #dbeafe;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 4px 12px rgba(15,23,42,0.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown("<div class='main-title'>🏠 Property Planning & Price Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Smart Land & House Price Estimation</div>", unsafe_allow_html=True)


CITY_DATA = {
    "Chennai": {"zone": "South India", "rate": 2100, "market_label": "Metro living zone", "maps_url": "https://www.google.com/maps/search/chennai+property+area"},
    "Bengaluru": {"zone": "South India", "rate": 2300, "market_label": "High-demand urban zone", "maps_url": "https://www.google.com/maps/search/bengaluru+property+area"},
    "Hyderabad": {"zone": "South India", "rate": 1900, "market_label": "Growing metro zone", "maps_url": "https://www.google.com/maps/search/hyderabad+property+area"},
    "Mumbai": {"zone": "West India", "rate": 3200, "market_label": "Premium metro zone", "maps_url": "https://www.google.com/maps/search/mumbai+property+area"},
    "Delhi": {"zone": "North India", "rate": 2600, "market_label": "Capital city zone", "maps_url": "https://www.google.com/maps/search/delhi+property+area"},
    "Pune": {"zone": "West India", "rate": 2000, "market_label": "Fast-growing city zone", "maps_url": "https://www.google.com/maps/search/pune+property+area"},
    "Kolkata": {"zone": "East India", "rate": 1700, "market_label": "Established metro zone", "maps_url": "https://www.google.com/maps/search/kolkata+property+area"},
    "Jaipur": {"zone": "North India", "rate": 1500, "market_label": "Emerging urban zone", "maps_url": "https://www.google.com/maps/search/jaipur+property+area"},
    "Lucknow": {"zone": "North India", "rate": 1400, "market_label": "Developing city zone", "maps_url": "https://www.google.com/maps/search/lucknow+property+area"},
    "Ahmedabad": {"zone": "West India", "rate": 1600, "market_label": "Commercial growth zone", "maps_url": "https://www.google.com/maps/search/ahmedabad+property+area"},
    "Coimbatore": {"zone": "South India", "rate": 1500, "market_label": "Smart city zone", "maps_url": "https://www.google.com/maps/search/coimbatore+property+area"},
    "Visakhapatnam": {"zone": "South India", "rate": 1400, "market_label": "Coastal growth zone", "maps_url": "https://www.google.com/maps/search/visakhapatnam+property+area"},
    "Nagpur": {"zone": "Central India", "rate": 1200, "market_label": "Affordable growth zone", "maps_url": "https://www.google.com/maps/search/nagpur+property+area"},
    "Indore": {"zone": "Central India", "rate": 1250, "market_label": "Economic growth zone", "maps_url": "https://www.google.com/maps/search/indore+property+area"},
    "Patna": {"zone": "East India", "rate": 1100, "market_label": "Emerging residential zone", "maps_url": "https://www.google.com/maps/search/patna+property+area"},
}

BLUEPRINT_FACTORS = {
    "1 BHK": 1.0,
    "2 BHK": 1.45,
    "3 BHK": 1.9,
    "Duplex": 2.4,
    "Villa": 3.2,
}


def estimate_land_area(budget: float, city: str) -> float:
    rate_per_sqft = CITY_DATA.get(city, {"rate": 1400})["rate"]
    land_area = (budget * 0.45) / rate_per_sqft
    return round(land_area, 2)


def classify_land(budget: float, city: str) -> str:
    area = estimate_land_area(budget, city)
    if area < 500:
        return "Small Land Plot"
    if area < 1200:
        return "Medium Land Plot"
    return "Large Land Plot"


def predict_total_cost(budget: float, city: str, blueprint: str) -> float:
    area = estimate_land_area(budget, city)
    city_rate = CITY_DATA.get(city, {"rate": 1400})["rate"]
    blueprint_factor = BLUEPRINT_FACTORS.get(blueprint, 1.5)
    land_value = area * city_rate * 0.75
    construction_cost = area * blueprint_factor * 120
    total = land_value + construction_cost
    return round(total, 2)


def get_budget_blueprints(budget: float):
    recommendations = []
    for name, factor in BLUEPRINT_FACTORS.items():
        estimated_cost = (budget * 0.6) / factor
        if estimated_cost <= budget:
            recommendations.append({"blueprint": name, "estimated_cost": round(estimated_cost, 2)})
    return recommendations


def get_ai_assistant_message(name: str, city: str, budget: float, blueprint: str) -> str:
    city_rate = CITY_DATA.get(city, {"rate": 1400})["rate"]
    safety_score = 8.2 if city in ["Chennai", "Bengaluru", "Hyderabad", "Pune", "Coimbatore"] else 7.5
    commute_score = 8.5 if city in ["Bengaluru", "Pune", "Hyderabad", "Chennai"] else 7.2
    affordable_blueprints = get_budget_blueprints(budget)
    preferred = affordable_blueprints[0]["blueprint"] if affordable_blueprints else blueprint
    area = estimate_land_area(budget, city)

    message = (
        f"Hello {name or 'there'}, I’m your property assistant. Based on your budget of ₹{budget:,.0f} and the city {city}, "
        f"this location looks {CITY_DATA[city]['market_label']}. Your estimated land area is about {area:,.0f} sq ft, and the city price band is around ₹{city_rate:,.0f} per sq ft. "
        f"For family comfort, I recommend checking the area on live maps and verifying the local environment before finalizing the deal. "
        f"Based on safety and commute comfort, this location has a safety score of {safety_score:.1f}/10 and a transport convenience score of {commute_score:.1f}/10. "
        f"To reduce travel costs and improve daily convenience, I suggest choosing a property near schools, hospitals, and a transit route. "
        f"If your budget is tight, the best matching option is {preferred}, which is more feasible and still practical for a family."
    )
    return message


with st.form("property_form"):
    st.subheader("1) Customer Information")
    name = st.text_input("Customer Name", placeholder="Enter full name")
    budget = st.number_input("Budget (INR)", min_value=200000, max_value=10000000, value=1500000, step=50000)

    st.subheader("2) City, Location & Land Planning")
    city = st.selectbox("Select City", list(CITY_DATA.keys()))
    city_zone = CITY_DATA[city]["zone"]
    city_rate = CITY_DATA[city]["rate"]
    city_note = CITY_DATA[city]["market_label"]
    city_map_url = CITY_DATA[city]["maps_url"]

    land_area = estimate_land_area(budget, city)
    land_category = classify_land(budget, city)

    st.info(
        f"Hello {name or 'Customer'}, with your budget of ₹{budget:,.0f} in {city}, the land recommendation is about {land_area:,.0f} sq ft. "
        f"This is classified as a {land_category}. Current price band in {city} is roughly ₹{city_rate:,.0f} per sq ft ({city_note})."
    )

    st.markdown(f"**Live location check:** [Open Google Maps for {city}]({city_map_url})")

    st.subheader("3) House Blueprint")
    blueprint = st.selectbox("Choose Blueprint", list(BLUEPRINT_FACTORS.keys()))

    submitted = st.form_submit_button("Predict Property Price", use_container_width=True)

if submitted:
    estimated_total = predict_total_cost(budget, city, blueprint)
    budget_blueprints = get_budget_blueprints(budget)
    assistant_message = get_ai_assistant_message(name, city, budget, blueprint)

    investment_note = (
        "This estimate includes land value and construction planning based on your selected city and blueprint. "
        "It is a practical planning estimate for final-year project demonstration."
    )

    st.success(f"Estimated Property Price: ₹{estimated_total:,.0f}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Budget", f"₹{budget:,.0f}")
    col2.metric("Land Area", f"{land_area:,.0f} sq ft")
    col3.metric("City", city)

    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    st.write(f"Customer: {name or 'Customer'}")
    st.write(f"City: {city} ({city_zone})")
    st.write(f"Price Band: ₹{city_rate:,.0f} per sq ft")
    st.write(f"Recommended Land Category: {land_category}")
    st.write(f"Selected Blueprint: {blueprint}")
    st.write(f"Estimated Market Value: ₹{estimated_total:,.0f}")
    st.write(investment_note)
    st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("AI Property Advisor")
    st.markdown(
        f"<div class='info-box'><p style='font-size: 1.05rem; line-height: 1.7;'>{assistant_message}</p></div>",
        unsafe_allow_html=True,
    )

    st.subheader("Budget-Friendly Blueprint Suggestions")
    if budget_blueprints:
        for item in budget_blueprints[:5]:
            st.write(f"- {item['blueprint']}: suitable budget estimate around ₹{item['estimated_cost']:,.0f}")
    else:
        st.write("No affordable blueprint suggestion available in this range. Try reducing the target area or selecting a more affordable city.")

    st.subheader("Available Cities and Price Ranges")
    city_table = []
    for city_name, details in CITY_DATA.items():
        city_table.append({
            "City": city_name,
            "Zone": details["zone"],
            "Price per sq ft": f"₹{details['rate']:,.0f}",
            "Market Type": details["market_label"],
        })
    st.dataframe(city_table, use_container_width=True)

else:
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    st.write("Step 1: Enter the customer name and budget.")
    st.write("Step 2: Select the city to view available pricing and land estimates.")
    st.write("Step 3: Choose a blueprint and predict the final property value.")
    st.write("Step 4: If the budget is low, the app suggests affordable blueprint options.")
    st.markdown("</div>", unsafe_allow_html=True)
