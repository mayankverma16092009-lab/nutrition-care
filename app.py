import random
import streamlit as st

st.set_page_config(
    page_title="Nutrition Care",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------- Styling -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp { background: linear-gradient(145deg, #f5faf7 0%, #f7f8fc 55%, #eef7f3 100%); }
.block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1180px; }
h1, h2, h3 { font-family: 'Manrope', sans-serif; color: #173b32; }
.hero {
    padding: 2rem 2.1rem; border-radius: 24px;
    background: linear-gradient(120deg, #123d32 0%, #1c6651 58%, #3b9270 100%);
    color: white; margin-bottom: 1.4rem;
    box-shadow: 0 14px 35px rgba(22, 75, 59, .15);
}
.hero h1 { color: white; font-size: clamp(2rem, 4vw, 3.1rem); margin: 0 0 .35rem 0; }
.hero p { color: #e1f2e9; font-size: 1.05rem; margin: 0; }
.eyebrow { color: #b9e6d1; font-size: .78rem; font-weight: 700; letter-spacing: .13em; text-transform: uppercase; }
.panel {
    background: white; border: 1px solid #e4eee8; border-radius: 18px;
    padding: 1.1rem 1.25rem; box-shadow: 0 5px 18px rgba(20, 65, 50, .045);
}
.small-muted { color: #657b72; font-size: .92rem; }
.meal-card {
    background: white; border: 1px solid #e3eee7; border-left: 5px solid #31936e;
    padding: 1rem 1.1rem; border-radius: 14px; margin: .65rem 0;
}
.meal-title { color: #1b5944; font-weight: 700; font-size: 1.03rem; }
div[data-testid="stMetric"] {
    background: white; padding: 1rem; border: 1px solid #e3eee7;
    border-radius: 15px;
}
.stButton > button, .stFormSubmitButton > button {
    background: #1c7657; color: white; border: 0; border-radius: 11px;
    padding: .55rem 1.15rem; font-weight: 700;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    background: #155b43; color: white; border: 0;
}
[data-testid="stSidebar"] { background: #f0f7f3; }
hr { border-color: #e2ece6; }
</style>
""", unsafe_allow_html=True)

# ----------------------------- Content data -----------------------------
FOOD_OPTIONS = {
    "Breakfast": [
        {"name": "Vegetable oats with plain curd", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": ["Dairy"], "staple": ["Both", "Roti / whole grains"]},
        {"name": "Moong dal chilla with mint chutney", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": [], "staple": ["Both", "Roti / whole grains"]},
        {"name": "Idli with sambar and vegetables", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": [], "staple": ["Both", "Rice"]},
        {"name": "Egg bhurji with whole-wheat toast", "types": ["Eggetarian", "Non-vegetarian"], "tags": ["Egg", "Wheat / gluten"], "staple": ["Both", "Roti / whole grains"]},
        {"name": "Besan chilla with tomato chutney", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": [], "staple": ["Both", "Roti / whole grains"]},
    ],
    "Lunch": [
        {"name": "Roti, dal, seasonal vegetables and salad", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": ["Wheat / gluten"], "staple": ["Both", "Roti / whole grains"]},
        {"name": "Rice, rajma and cucumber salad", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": [], "staple": ["Both", "Rice"]},
        {"name": "Rice, dal, mixed vegetables and curd", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": ["Dairy"], "staple": ["Both", "Rice"]},
        {"name": "Roti with chicken curry and vegetables", "types": ["Non-vegetarian"], "tags": ["Wheat / gluten"], "staple": ["Both", "Roti / whole grains"]},
        {"name": "Vegetable khichdi with salad", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": [], "staple": ["Both", "Rice"]},
    ],
    "Evening snack": [
        {"name": "Roasted chana with water", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": [], "staple": ["Both", "Roti / whole grains", "Rice"]},
        {"name": "One serving of whole fruit with a few seeds", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": ["Seeds"], "staple": ["Both", "Roti / whole grains", "Rice"]},
        {"name": "Sprouts and vegetable chaat", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": [], "staple": ["Both", "Roti / whole grains", "Rice"]},
        {"name": "Plain unsweetened curd", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": ["Dairy"], "staple": ["Both", "Roti / whole grains", "Rice"]},
    ],
    "Dinner": [
        {"name": "Roti with dal and cooked vegetables", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": ["Wheat / gluten"], "staple": ["Both", "Roti / whole grains"]},
        {"name": "Vegetable and moong dal khichdi with salad", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": [], "staple": ["Both", "Rice"]},
        {"name": "Rice with chana curry and vegetables", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": [], "staple": ["Both", "Rice"]},
        {"name": "Grilled chicken with vegetables and a grain", "types": ["Non-vegetarian"], "tags": [], "staple": ["Both", "Roti / whole grains", "Rice"]},
        {"name": "Paneer bhurji with roti and salad", "types": ["Vegetarian", "Eggetarian", "Non-vegetarian"], "tags": ["Dairy", "Wheat / gluten"], "staple": ["Both", "Roti / whole grains"]},
    ],
}

def eligible_meals(meal, diet, avoid, staple):
    candidates = [
        item for item in FOOD_OPTIONS[meal]
        if diet in item["types"]
        and not any(tag in item["tags"] for tag in avoid)
        and staple in item["staple"]
    ]
    return candidates

def make_plan(diet, avoid, staple, style):
    plan = {}
    for meal in ["Breakfast", "Lunch", "Evening snack", "Dinner"]:
        choices = eligible_meals(meal, diet, avoid, staple)
        if not choices:
            # Do not silently ignore restrictions: report that a dietitian should review.
            plan[meal] = None
        else:
            plan[meal] = random.choice(choices)["name"]
    return plan

def hero(title, subtitle, eyebrow="NUTRITION EDUCATION"):
    st.markdown(
        f'<div class="hero"><div class="eyebrow">{eyebrow}</div>'
        f'<h1>{title}</h1><p>{subtitle}</p></div>',
        unsafe_allow_html=True,
    )

# ----------------------------- Sidebar -----------------------------
with st.sidebar:
    st.markdown("## 🥗 Nutrition Care")
    st.caption("Diabetes nutrition support & awareness")
    st.divider()
    page = st.radio(
        "Explore modules",
        [
            "Home",
            "Healthy Plate Guide",
            "Indian Food Guide",
            "Nutrition Label Reader",
            "Blood Glucose Education",
            "Meal Examples",
            "Knowledge Quiz",
            "Diet Plan Generator",
        ],
        label_visibility="visible",
    )
    st.divider()
    st.caption("Educational project • Not a medical service")

# ----------------------------- Pages -----------------------------
if page == "Home":
    hero("Eat well. Learn better.", "A simple learning space for understanding food choices and diabetes nutrition.")
    c1, c2, c3 = st.columns(3)
    c1.metric("Learning modules", "7")
    c2.metric("Meal categories", "4")
    c3.metric("Focus", "Nutrition awareness")
    st.write("")
    st.markdown("### Welcome to Nutrition Care")
    st.write("Explore practical nutrition concepts, learn how to read food labels, and see balanced Indian meal examples.")
    left, right = st.columns([1.15, 0.85])
    with left:
        st.markdown('<div class="panel"><h3>What you can learn</h3><p>• Understanding carbohydrates and fibre</p><p>• Making informed food choices</p><p>• Reading nutrition labels</p><p>• Understanding blood glucose</p><p>• Exploring meal ideas and food preferences</p></div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div class="panel"><h3>Start here</h3><p class="small-muted">Use the Diet Plan Generator to answer a short food-preference questionnaire and receive general meal ideas.</p></div>', unsafe_allow_html=True)
        if st.button("Open Diet Plan Generator", use_container_width=True):
            st.session_state["jump_to_diet"] = True
            st.rerun()

elif page == "Healthy Plate Guide":
    hero("Healthy Plate Guide", "A visual way to think about variety and balance at mealtimes.")
    st.markdown("""
    <div class="panel">
      <h3>Build a balanced plate</h3>
      <p><b>½ plate:</b> non-starchy vegetables, such as leafy greens, beans, cauliflower and cucumber.</p>
      <p><b>¼ plate:</b> protein foods, such as dal, beans, tofu, eggs, fish or chicken.</p>
      <p><b>¼ plate:</b> carbohydrate-containing foods, such as roti, rice, millets or other grains.</p>
      <p class="small-muted">This is a general teaching model, not a personal prescription. Individual needs can differ.</p>
    </div>
    """, unsafe_allow_html=True)
    st.info("People using insulin or glucose-lowering medicines should ask their healthcare team before making major changes to meal timing or carbohydrate intake.")

elif page == "Indian Food Guide":
    hero("Indian Food Guide", "Explore familiar foods and the nutrients they can contribute.")
    food_data = {
        "Roti": "Whole-wheat roti provides carbohydrates and some fibre. Whole-grain choices can contribute to a balanced meal.",
        "Rice": "Rice is a carbohydrate-containing staple. Portion size and what is served alongside it matter.",
        "Dal": "Dal provides plant protein, carbohydrates and dietary fibre.",
        "Curd": "Plain curd provides protein and calcium. Choose an option that suits your dietary needs.",
        "Chana": "Chana provides plant protein, carbohydrates and fibre.",
        "Spinach": "Spinach contributes fibre and several vitamins and minerals.",
        "Apple": "An apple provides carbohydrates, water and fibre; whole fruit is generally preferable to juice."
    }
    food = st.selectbox("Select an Indian food", list(food_data.keys()))
    st.markdown(f'<div class="panel"><h3>{food}</h3><p>{food_data[food]}</p></div>', unsafe_allow_html=True)

elif page == "Nutrition Label Reader":
    hero("Nutrition Label Reader", "Enter label values to organize and understand the information.")
    st.caption("Use values from the same serving size shown on the package.")
    serving = st.number_input("Serving size (grams)", min_value=1, max_value=5000, value=100)
    carbs = st.number_input("Total carbohydrates (g)", min_value=0.0, max_value=1000.0, value=0.0, step=0.5)
    fibre = st.number_input("Dietary fibre (g)", min_value=0.0, max_value=1000.0, value=0.0, step=0.5)
    sugar = st.number_input("Added sugar (g)", min_value=0.0, max_value=1000.0, value=0.0, step=0.5)
    if st.button("Review nutrition information"):
        st.subheader("Label summary")
        a, b, c = st.columns(3)
        a.metric("Carbohydrates", f"{carbs:g} g")
        b.metric("Dietary fibre", f"{fibre:g} g")
        c.metric("Added sugar", f"{sugar:g} g")
        if fibre > carbs:
            st.warning("Check the values entered: fibre is greater than total carbohydrates.")
        else:
            st.info(f"Values entered for a {serving} g serving. Compare products using the same serving size and review the full ingredient list.")

elif page == "Blood Glucose Education":
    hero("Blood Glucose Education", "Understand the basics of glucose, food and the body.")
    with st.expander("What is blood glucose?", expanded=True):
        st.write("Blood glucose is the amount of glucose (a type of sugar) in the blood. The body uses glucose as an important source of energy.")
    with st.expander("How can carbohydrates affect blood glucose?"):
        st.write("Carbohydrates are digested into glucose and can raise blood glucose after eating. The effect varies with the food, portion, meal composition, medicines and individual factors.")
    with st.expander("What does insulin do?"):
        st.write("Insulin is a hormone that helps glucose move from the bloodstream into cells.")
    with st.expander("Why is monitoring important?"):
        st.write("A healthcare professional may recommend monitoring to understand patterns and guide care. Follow the monitoring plan provided by your healthcare team.")

elif page == "Meal Examples":
    hero("Educational Indian Meal Examples", "Examples that combine different food groups.")
    examples = [
        ("Breakfast", "Vegetable poha with peanuts (if suitable) and plain curd."),
        ("Lunch", "Roti, dal, seasonal sabzi and cucumber salad."),
        ("Snack", "Roasted chana or a serving of whole fruit."),
        ("Dinner", "Vegetable khichdi with a side of salad or cooked vegetables."),
    ]
    for name, desc in examples:
        st.markdown(f'<div class="meal-card"><div class="meal-title">{name}</div>{desc}</div>', unsafe_allow_html=True)
    st.caption("These are general examples. Allergies, medical needs, culture, budget and personal preferences should be considered.")

elif page == "Knowledge Quiz":
    hero("Nutrition Knowledge Quiz", "Check your understanding of a few basic concepts.")
    with st.form("quiz_form"):
        q1 = st.radio("1. Which nutrient generally has the most direct effect on blood glucose after eating?", ["Carbohydrates", "Water", "Vitamin C"])
        q2 = st.radio("2. Which food is a source of dietary fibre?", ["Lentils", "Soft drinks", "Candy"])
        q3 = st.radio("3. Should everyone with diabetes follow exactly the same meal plan?", ["Yes", "No"])
        submitted = st.form_submit_button("Submit answers")
    if submitted:
        score = sum([q1 == "Carbohydrates", q2 == "Lentils", q3 == "No"])
        st.success(f"Your score: {score}/3")
        if score == 3:
            st.write("Excellent work! You understand these key ideas.")
        else:
            st.write("Good effort. Review the learning modules and try again.")

elif page == "Diet Plan Generator":
    hero("Diet Plan Generator", "Answer the questionnaire to receive general Indian meal ideas based on your food preferences.")
    st.info("This tool creates educational meal suggestions only. It does not calculate calories, prescribe portions, diagnose diabetes or replace advice from a registered dietitian.")
    with st.form("diet_questionnaire"):
        st.markdown("### 1. Food preferences")
        diet = st.selectbox("Which type of diet do you prefer?", ["Vegetarian", "Eggetarian", "Non-vegetarian"])
        staple = st.selectbox("Which staple foods do you prefer?", ["Both", "Roti / whole grains", "Rice"])
        style = st.selectbox("Which meal style do you prefer?", ["Traditional Indian", "Simple and easy meals"])
        st.markdown("### 2. Foods to avoid")
        avoid = st.multiselect("Select any allergies or foods you need to avoid", ["Dairy", "Egg", "Wheat / gluten", "Peanuts", "Soy", "Fish", "Seeds"])
        st.markdown("### 3. Meal routine")
        meal_pattern = st.radio("Which routine sounds closest to yours?", ["3 meals", "3 meals + 1 snack", "3 meals + 2 snacks"], horizontal=True)
        submitted = st.form_submit_button("✨ Generate my meal ideas", use_container_width=True)

    if submitted:
        st.session_state["diet_result"] = {
            "diet": diet, "staple": staple, "style": style,
            "avoid": avoid, "meal_pattern": meal_pattern,
            "plan": make_plan(diet, avoid, staple, style),
        }

    if "diet_result" in st.session_state:
        result = st.session_state["diet_result"]
        st.divider()
        st.markdown("### Your generated meal ideas")
        st.write(f"**Food preference:** {result['diet']}  ·  **Staple preference:** {result['staple']}  ·  **Routine:** {result['meal_pattern']}")
        if result["avoid"]:
            st.write("**Foods selected to avoid:** " + ", ".join(result["avoid"]))
        else:
            st.write("**Foods selected to avoid:** None selected")
        cols = st.columns(2)
        for idx, meal in enumerate(["Breakfast", "Lunch", "Evening snack", "Dinner"]):
            with cols[idx % 2]:
                suggestion = result["plan"][meal]
                if suggestion:
                    st.markdown(f'<div class="meal-card"><div class="meal-title">{meal}</div>{suggestion}</div>', unsafe_allow_html=True)
                else:
                    st.warning(f"No matching {meal.lower()} suggestion was found for all selected restrictions. Please ask a registered dietitian to help choose a safe alternative.")
        st.caption("The generator selects from a small example menu. It does not verify ingredient brands, cross-contamination, nutrient totals or medical suitability.")
        st.warning("If the person has diabetes, kidney disease, food allergies, is pregnant, takes glucose-lowering medicine, or has other medical needs, a registered dietitian or healthcare professional should review any meal changes. Do not change medication based on this website.")
        if st.button("Clear generated plan"):
            del st.session_state["diet_result"]
            st.rerun()

# ----------------------------- Footer -----------------------------
st.divider()
st.caption("Nutrition Care | Healthcare education project | General information only — not a substitute for professional medical advice.")
