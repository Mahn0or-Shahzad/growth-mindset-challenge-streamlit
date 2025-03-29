import streamlit as st
import random

st.set_page_config(page_title = "🧠 Growth Mindset App" , layout = "wide")
st.title("🌟 Growth Mindset Challenge")
st.write("Welcome to the Growth Mindset Quiz! let's how you think about challenges and learning. 🚀")
st.sidebar.title("📌 Menu")
page = st.sidebar.selectbox("📖 Choose a page",[str(option) for option in ["🏠 Home","📝 Quiz","💡 Motivation"]])

if page == "🏠 Home":
    st.header(" What is a Growth Mindset?")
    st.write("A growth mindset is the belief that abilities and intelligence can be developed though dedication,efforts,and learning rather than being fixed or innate 📚✨")
elif page == "📝 Quiz":
    st.header("🧐 Mindset Quiz")
    st.write("Answer the following questions to know your mindset.✅")
elif page == "💡 Motivation":
    st.header("🔥 Daily Motivation")
    st.write("Here you'll see daily motivational quotes and success stories!💪✨")

if page == "📝 Quiz":
    st.header(" 🧠Growth Mindset Quiz")
    st.success(f"🎉 Welcome! let's start the quiz 🚀")

    score = 0

    Q1 = st.radio("1️⃣  🔍 When faced with a dificult task,do you:",
                 ["1. Give up easily because you feel it's too hard😔",
                  "2. See it as a challenge and an opportunity to learn and improve🚀" ,
                  "3. Accept the task as a reflection of your abilities🪞" ,
                  "4. Avoit the task altogether❌"] , index = None)
    if Q1 == "2. See it as a challenge and an opportunity to learn and improve🚀":
        score += 1

    Q2 = st.radio("2️⃣  ❓ When you make a mistake,do you:",
                 ["1. Feel discouraged and see it as a sign of your incompetence😞",
                  "2. Use it as a learning experience and try to understand what went wrong🎓",
                  "3. Blame others or the circumstances🤷",
                  "4. Ignore the mistake and move on without learning from it🚶‍♀️"] , index = None)
    if Q2 == "2. Use it as a learning experience and try to understand what went wrong🎓":
        score += 1

    Q3 = st.radio("3️⃣  🧐 How do you view intelligence:",
                 ["1. As a fixed trait that you are born🏷️" ,
                  "2. As something that is determined by your environment🌎",
                  "3. As something that is not important for success🚫",
                  "4. As something that can be developed through effort and learning💪"] , index = None)
    if Q3 == "4. As something that can be developed through effort and learning💪":   
        score += 1

    Q4 = st.radio("4️⃣  💡 When someone else succeeds, do you:" ,
                 ["1. Feel inspired and motivated to learn from them🌟" ,
                  "2. Feel envious or discouraged😡" ,
                  "3. Dismiss their success as luck or unfairness🎲",
                  "4. Ignore their success altogether🙈"] , index = None)
    if Q4 == "1. Feel inspired and motivated to learn from them🌟":
        score += 1

    Q5 = st.radio("5️⃣  🗣️ How do you handle constructive criticism:" ,
                 ["1. Take it personally and feel hurt😢" ,
                  "2. Ignore it because you know what you're doing🙉" ,
                  "3. Appreciate it and use it to improve🎯" ,
                  "4. Get defensive and argue against it🛑"] , index = None)
    if Q5 == "3. Appreciate it and use it to improve🎯":
        score += 1

    Q6 = st.radio("6️⃣  📚 When learning something new, do you:" ,
                 ["1. Stick to things you're already good at🛑" ,
                  "2. Feel frustrated and assume you're not capable😖" ,
                  "3. Give up if you don't get it right immediately🏳️" ,
                  "4. Embrace the challenge and practice until you improve🚀"] , index = None)
    if Q6 == "4. Embrace the challenge and practice until you improve🚀":
        score +=1

    Q7 = st.radio("7️⃣  👀 How do you react when you see someone working harder than you:" ,
                 ["1. Feel motivated to push yourself and improve💪" ,
                  "2. Think they are wasting time,talent matters more🧠" ,
                  "3. Assume they are only working hard because they are not naturally talented🤔" ,
                  "4. Ignore them,it's their own journey🚶‍♀️"] , index = None)
    if Q7 == "1. Feel motivated to push yourself and improve💪":
        score += 1 

    Q8 = st.radio("8️⃣  🔄 If you fail at something at multiple times,what do you do:" ,
                 ["1. Accept that you're not good at it and stop trying❌" ,
                  "2. Blame the situation or external factors⚖️" ,
                  "3. Try different approaches and keep practicing until you succeed🏆" ,
                  "4. Avoid similar challenges in the future⏭️"] , index = None)  
    if Q8 == "3. Try different approaches and keep practicing until you succeed🏆":
        score +=1 
       
    Q9 = st.radio("9️⃣  💪 What is your opinion on effort:" ,
                 ["1. Some people are just naturally talented, efforth doesn't change much🧠" ,
                  "2. If you need to put in alot of effort,it means you're not good at it❌" ,
                  "3. Only certain skills are worth putting effort into🎯" ,
                  "4. Hardwork and effort can improve skills over time🚀"] , index = None)
    if Q9 == "4. Hardwork and effort san improve skills over time🚀":
        score += 1

    Q10 = st.radio("🔟  🔄 How do you handle setbacks:" ,
                   ["1. Give up and move on to something easier🏳️" ,
                    "2. Use setbacks as a way to reflect and try again smarter🔄" ,
                    "3. Blame others or external circumstances for your failure⚖️" ,
                    "Get frustrated and avoit similar challenges in the future😖"] , index = None)
    if Q10 == "2. Use setbacks as a way to reflect and try again smarter🔄":
        score += 1

    if st.button("Submit"):
        st.write(f"🎯 Your score is: {score}/10")

        if score == 10:
            st.success("⭐ **Excelent!** "
            "you have a strong mindset! 🚀")
        elif score >= 7:
            st.info("😊 **Great job!**"
            "you have a good growth mindset! 🔥")
        elif score > 4:
            st.warning("⚠️ **You're on the right track!**"
            "Try to challenge yourself more. 💡")
        else:
            st.error("❌ **You may have a fixed mindset.**")

        st.session_state.score = score

if page == "💡 Motivation":
    st.header("💖 Daily Motivation")

    quotes = [
        "🔥 Failure is not the opposite success; it's part of success! 🚀" ,
        "💭 The only limit to our realization of tomorrow is our doubt of today! 🌟" ,
        "💡 Success in not final, failure is not fatal, it is the courage to continue that counts! 🎯" ,
        "🏆 Believe in youself and all that you are know that there is something inside you that is greater than any obstacle! 💪" ,
        "💯 Your mindset is everything stay positive,work hard,and make it happen! 🚀"
]
    success_stories = [
        "💡 **Thomas Edison**  failed 10,000 times before inventing the light bulb! 🔥 He said, 'I have not failed. I've just found 10,000 ways that not work!' 🌟" ,
        "🚀 **Elon Musk** was rejected by multiple companies before lanching Spacex and Tesla! 💥 His first three rocket launches failed, but he never gave up! 🌎✨" ,
        "📚 **J.K.Rowling** was rejected by 12 publishers before **Harry Potter** became a success! 🧙 Today, she is one of the most famous authors in the world! 📚✨" ,
        "💻 **Steve Jobs** was fired from Apple,the company he co-founded🚫🍏. Years later, He returned and made Apple a global tech leader! 💻🚀" ,
        "🥇 **Oprah Winfrey** was fired from her first TV job for being 'unfit for television.📺💔' She became one of the most influential TV personalities ever! 🌟🎤"
    ]

    st.subheader("📢 Today's Motivational Quote:")
    st.success(random.choice(quotes))
    st.subheader("📖 Success Story:")
    st.info(random.choice(success_stories))