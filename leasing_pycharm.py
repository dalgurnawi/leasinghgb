# Importing packages

import streamlit as st
from class_leasing import Leasing

# Title for the app
st.title("Leasing treatment according to HGB")

# Information submission form for the app
with st.form(key='my_form'):

    cost = st.number_input("Please enter the acquisition cost of the asset",
                                   min_value=None,
                                   max_value=None,
                                   value=300,
                                   step=None,
                                   format=None,
                                   key=None,
                                   help=None,
                                   on_change=None,
                                   args=None,
                                   kwargs=None,
                                   disabled=False)


    interest = st.number_input("Please enter the interest rate of leasing the asset, as stipulated per the contract",
                                   min_value=None,
                                   max_value=None,
                                   value=0.0,
                                   step=None,
                                   format=None,
                                   key=None,
                                   help=None,
                                   on_change=None,
                                   args=None,
                                   kwargs=None,
                                   disabled=False)/100


    monthly_rate = st.number_input("Please enter the monthly rate for leasing the asset",
                                   min_value=None,
                                   max_value=None,
                                   value=300,
                                   step=None,
                                   format=None,
                                   key=None,
                                   help=None,
                                   on_change=None,
                                   args=None,
                                   kwargs=None,
                                   disabled=False)

    duration = st.number_input("Please enter the duration of the leasing agreement in months",
                               min_value=None,
                               max_value=None,
                               value=0,
                               step=None,
                               format=None,
                               key=None,
                               help="If there is no fixed duration, enter 0",
                               on_change=None,
                               args=None,
                               kwargs=None,
                               disabled=False)

    pen_can = st.selectbox("Is a penalty applied in the event of a cancellation?",
                           ("Yes", "No"),
                           index=0,
                           key=None,
                           help=None,
                           on_change=None,
                           args=None,
                           kwargs=None,
                           disabled=False)

    useful_life = st.number_input("In months, what is the economic useful life of the asset? ",
                                  min_value=None,
                                  max_value=None,
                                  value=12,
                                  step=None,
                                  format=None,
                                  key=None,
                                  help='Enter 0 if not applicable',
                                  on_change=None,
                                  args=None,
                                  kwargs=None,
                                  disabled=False)

    option = st.selectbox("What options does the contract specify at the end of the lease?",
                          ("No options", "Purchase Option", "Extension Option", "Special Leasing"),
                          index=0,
                          key=None,
                          help="Enter 'No options' if not applicable",
                          on_change=None,
                          args=None,
                          kwargs=None,
                          disabled=False)

    purchase_price = st.number_input(
        "If you have selected 'Purchase Option' to the question above, what is the purchase price? ",
        min_value=None,
        max_value=None,
        value=1000,
        step=None,
        format=None,
        key=None,
        help='Enter 0 if not applicable',
        on_change=None,
        args=None,
        kwargs=None,
        disabled=False)

    net_book_value = st.number_input("What is the expected net book value at the end of the agreement?",
                                     min_value=None,
                                     max_value=None,
                                     value=1000,
                                     step=None,
                                     format=None,
                                     key=None,
                                     help='Enter 0 if not applicable',
                                     on_change=None,
                                     args=None,
                                     kwargs=None,
                                     disabled=False)

    ext_rate = st.number_input(
        "If you have selected 'Extension Option' to the question above, what is the monthly rate for the extended period?",
        min_value=None,
        max_value=None,
        value=100,
        step=None,
        format=None,
        key=None,
        help='Enter 0 if not applicable',
        on_change=None,
        args=None,
        kwargs=None,
        disabled=False)

    market_rate = st.number_input(
        "If you have selected 'Extension Option' to the question above, what is the monthly market rate for the extended period for a similar asset?",
        min_value=None,
        max_value=None,
        value=100,
        step=None,
        format=None,
        key=None,
        help='Enter 0 if not applicable',
        on_change=None,
        args=None,
        kwargs=None,
        disabled=False)

    submit_button =st.form_submit_button(label='Submit for analysis')

# Running the code after the form has been completed



lease_1 = Leasing(cost,
                 monthly_rate,
                 duration,
                 pen_can,
                 option,
                 useful_life,
                 purchase_price,
                 net_book_value,
                 ext_rate,
                 market_rate,
                 interest)

result = lease_1.lease(
                 monthly_rate,
                 duration,
                 pen_can,
                 option,
                 useful_life,
                 purchase_price,
                 net_book_value,
                 ext_rate,
                 market_rate,)

journal_entries = lease_1.journals(cost,
                 monthly_rate,
                 duration,
                 pen_can,
                 option,
                 useful_life,
                 purchase_price,
                 net_book_value,
                 ext_rate,
                 market_rate,
                 interest)

# Running the output after the code has been executed.
if submit_button:
    st.markdown(result)
    st.markdown(journal_entries)







