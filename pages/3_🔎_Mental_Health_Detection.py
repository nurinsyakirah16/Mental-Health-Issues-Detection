import streamlit as st

from MentalHealthDetection import vectorizer, best_model, label_encoder

st.set_page_config(page_title="Home", page_icon="🏠")
st.markdown("# Detect mental health issues based on social media text")

# Get user input
with st.form("text_form"):
    user_text = st.text_area("Enter your text here")
    enter_btn = st.form_submit_button("Enter")

# Create a button to trigger functions
if enter_btn:
    if not user_text:
        st.warning("Please enter your text")
    else:
        cleaned_input = vectorizer.transform([user_text]).toarray()
        output_result = best_model.predict(cleaned_input)
        proba = best_model.predict_proba(cleaned_input)

        predicted_class_label = label_encoder.inverse_transform(output_result)[0]
        confidence_score = proba.max()

        # Map the predicted label back to the original class
        recommendations = {
            "Stress": "Try relaxation techniques such as meditation or yoga, and prioritize self-care activities.",
            "Anxiety": "Practice deep breathing exercises and engage in regular physical activity.",
            "Depression": "Reach out to a trusted friend or family member and consider seeking professional help."
        }

        if predicted_class_label in recommendations:
            recommendation = recommendations[predicted_class_label]

        st.subheader("Prediction:")
        st.write("**Predicted Class:** ", predicted_class_label)
        st.write("**Confidence Score:** ", confidence_score)
        st.subheader("I recommend you to:")

        if predicted_class_label in recommendations:
            recommendation = recommendations[predicted_class_label]
        st.write(recommendation)
