# import streamlit as st
# import random

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="Number Guessing Game",
#     page_icon="🎯",
#     layout="centered"
# )

# # ---------------- CUSTOM CSS ----------------
# st.markdown("""
# <style>

# .main {
#     background-color: #0e1117;
# }

# .title {
#     text-align: center;
#     font-size: 3rem;
#     font-weight: bold;
#     background: linear-gradient(90deg,#00C6FF,#0072FF);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     margin-bottom: 10px;
# }

# .subtitle{
#     text-align:center;
#     color: #b0b0b0;
#     margin-bottom:30px;
# }

# .card {
#     padding: 25px;
#     border-radius: 20px;
#     background: rgba(255,255,255,0.05);
#     backdrop-filter: blur(10px);
#     border: 1px solid rgba(255,255,255,0.1);
# }

# .success-box {
#     padding:15px;
#     border-radius:15px;
#     background:#0f5132;
#     color:white;
#     font-weight:bold;
# }

# .error-box {
#     padding:15px;
#     border-radius:15px;
#     background:#842029;
#     color:white;
#     font-weight:bold;
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------- SESSION STATE ----------------
# if "number" not in st.session_state:
#     st.session_state.number = random.randint(1, 100)

# if "attempts" not in st.session_state:
#     st.session_state.attempts = 0

# if "game_over" not in st.session_state:
#     st.session_state.game_over = False

# # ---------------- HEADER ----------------
# st.markdown('<div class="title">🎯 Number Guessing Game</div>', unsafe_allow_html=True)

# st.markdown(
#     '<div class="subtitle">Guess the secret number between 1 and 100</div>',
#     unsafe_allow_html=True
# )

# # ---------------- CARD ----------------
# with st.container():
#     st.markdown('<div class="card">', unsafe_allow_html=True)

#     st.write(f"**Attempts Used:** {st.session_state.attempts}/5")
#     st.progress(st.session_state.attempts / 5)

#     guess = st.number_input(
#         "Enter your guess",
#         min_value=1,
#         max_value=100,
#         step=1
#     )

#     submit = st.button("🚀 Submit Guess", use_container_width=True)

#     if submit and not st.session_state.game_over:

#         st.session_state.attempts += 1

#         if guess == st.session_state.number:

#             st.markdown(
#                 f"""
#                 <div class="success-box">
#                 🎉 Congratulations!<br>
#                 You guessed the number in
#                 {st.session_state.attempts} attempts.
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#             st.balloons()
#             st.session_state.game_over = True

#         elif guess < st.session_state.number:
#             st.warning("📉 Too Low! Try a higher number.")

#         else:
#             st.warning("📈 Too High! Try a lower number.")

#         if (
#             st.session_state.attempts >= 5
#             and guess != st.session_state.number
#         ):

#             st.markdown(
#                 f"""
#                 <div class="error-box">
#                 😔 Game Over!<br>
#                 The correct number was
#                 <b>{st.session_state.number}</b>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#             st.balloons()
#             st.session_state.game_over = True

#     st.markdown("</div>", unsafe_allow_html=True)

# # ---------------- RESTART BUTTON ----------------
# if st.button("🔄 New Game", use_container_width=True):
#     st.session_state.number = random.randint(1, 100)
#     st.session_state.attempts = 0
#     st.session_state.game_over = False
#     st.rerun()

# # ---------------- FOOTER ----------------
# st.markdown("---")
# st.caption("Built with ❤️ using Streamlit")














'''hehe'''





import streamlit as st
import random

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="centered"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 50%,
        #1e1b4b 100%
    );
}

.main-title{
    text-align:center;
    font-size:60px;
    font-weight:800;
    background: linear-gradient(90deg,#ffffff,#fbbf24);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:20px;
    margin-bottom:20px;
}

.card{
    background:rgba(255,255,255,0.05);
    padding:25px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.08);
}

.result-win{
    text-align:center;
    padding:25px;
    border-radius:20px;
    background:rgba(34,197,94,0.15);
    border:1px solid rgba(34,197,94,0.5);
}

.result-lose{
    text-align:center;
    padding:25px;
    border-radius:20px;
    background:rgba(239,68,68,0.15);
    border:1px solid rgba(239,68,68,0.5);
}

.big-number{
    font-size:40px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -------------------- SESSION STATE --------------------
if "number" not in st.session_state:
    st.session_state.number = random.randint(1,100)

if "count" not in st.session_state:
    st.session_state.count = 0

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# -------------------- HEADER --------------------
st.markdown(
    '<div class="main-title">🎯 Number Guessing Game</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Guess the secret number between 1 and 100</div>',
    unsafe_allow_html=True
)

# -------------------- INFO CARD --------------------
st.markdown("""
<div class="card">
<h3>⭐ You have only 5 chances to guess the number!</h3>
</div>
""", unsafe_allow_html=True)

st.write("")

# -------------------- PROGRESS --------------------
st.write(f"### Attempts: {st.session_state.count}/5")
st.progress(st.session_state.count / 5)

# -------------------- GAME --------------------
if not st.session_state.game_over:

    guess = st.number_input(
        "Enter your number",
        min_value=1,
        max_value=100,
        step=1
    )

    submit = st.button(
        "🚀 Submit Guess",
        use_container_width=True
    )

    if submit:

        st.session_state.count += 1

        if guess == st.session_state.number:

            st.markdown(f"""
            <div class="result-win">
                <h1>🎉 YUPEEEEEE!!!! YOU WON!!</h1>
                <h3>You took {st.session_state.count} chances to win!</h3>
            </div>
            """, unsafe_allow_html=True)

            st.balloons()
            st.session_state.game_over = True

        elif guess > st.session_state.number:

            st.error("📈 Too High!! Guess Low.")

        else:

            st.error("📉 Too Low!! Guess High.")

        if (
            st.session_state.count >= 5
            and guess != st.session_state.number
        ):

            st.markdown(f"""
            <div class="result-lose">
                <h1>😢 OOPPSIIEEEEE!!!!! YOU LOST !!!</h1>
                <p>The actual number was</p>
                <div class="big-number">
                    {st.session_state.number}
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.balloons()
            st.session_state.game_over = True

# -------------------- PLAY AGAIN --------------------
st.write("")
st.write("")

if st.button("🔄 Play Again", use_container_width=True):

    st.session_state.number = random.randint(1,100)
    st.session_state.count = 0
    st.session_state.game_over = False

    st.rerun()

# -------------------- FOOTER --------------------
st.write("")
st.markdown(
    "<center>Made with ❤️ using Streamlit</center>",
    unsafe_allow_html=True
)