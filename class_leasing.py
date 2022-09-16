
class Leasing:

    def __init__(self,
                 cost,
                 monthly_rate,
                 duration,
                 pen_can,
                 option,
                 useful_life,
                 purchase_price,
                 net_book_value,
                 ext_rate,
                 market_rate,
                 interest):

        """Defining the variables used in the accounting treatment determination of leases.

        Args:

        cost (float) :  The acquisition costs of the asset.

        monthly_rate (float) : The current monthly rate for leasing the asset.

        duration (int): The total duration of the leasing agreement given in months.
                          If the leasing agreement is a rolling leasing agreement, then its
                          value will be 0.

        pen_can (str): Whether there is a penalty associated with early termination. Operating leases
                       usually do not have any cancellation fees. The responses are a Yes/ No.

        option (str): Select from "No options", "Purchase Option", "Extension Option", "Special Leasing"

        useful_life (int): The useful/ economic life of the asset given in months.

        purchase_price(float): The price to purchase the leased asset at the end of the agreement.

        net_book_value (float): The current net book value of the leased asset at the end of the
                                agreement.

        ext_rate(float): The leasing rate in an exercised lease extension option. Expressed in currency unit
                         per month.

        market_rate(float): The market rate for an equal asset for the lease extension period.

        interest(float): The interest rate associated with the finance lease

        """

        # Initialising the parameters

        self.monthly_rate = monthly_rate
        self.duration = duration
        self.pen_can = pen_can
        self.option = option
        self.useful_life = useful_life
        self.purchase_price = purchase_price
        self.net_book_value = net_book_value
        self.ext_rate = ext_rate
        self.market_rate = market_rate
        self.interest = interest
        self.cost = cost



    def lease(self, monthly_rate, duration, pen_can, option, useful_life, purchase_price, net_book_value, ext_rate,
              market_rate):
        global l

        if self.duration == 0 and self.pen_can == "No":


            output = (f"The lease is an operating lease and the asset is to be capitalised with the Lessor. The Lessee will book a monthly expense of CU {self.monthly_rate} to operating expenses.")


            l = 0  # Return zero for operating lease
            return output


        else:

            # Setting the treatment for no options
            if self.option == "No options":
                if self.duration < (0.4 * self.useful_life) or self.duration > (0.9 * self.useful_life):
                    output = "The lease is a finance lease and the asset is to be capitalised with the Lessee"
                    # global l
                    l = 1  # Return one for finance lease to be capitalised with Lessee
                    return output
                else:
                    output = "The lease is a finance lease and the asset is to be capitalised with the Lessor"
                    # global l
                    l = 2  # Return two for finance lease to be capitalised with Lessor
                    return output

            # Setting the treatment for Purchase Option
            elif self.option == "Purchase Option":

                if self.duration < (0.4 * self.useful_life) or self.duration > (0.9 * self.useful_life):
                    if self.purchase_price < self.net_book_value:
                        output = "The lease is a finance lease and the asset is to be capitalised with the Lessee"
                        # global l
                        l = 1
                        return output
                    else:
                        output = "The lease is a finance lease and the asset is to be capitalised with the Lessee"
                        # global l
                        l = 1
                        return output

                elif (0.4 * self.useful_life) < self.duration < (0.9 * self.useful_life):
                    if self.purchase_price < self.net_book_value:
                        output = "The lease is a finance lease and the asset is to be capitalised with the Lessee"
                        # global l
                        l = 1
                        return output
                    else:
                        output = "The lease is a finance lease and the asset is to be capitalised with the Lessor"
                        # global l
                        l = 2
                        return output

            # Setting the treatment for Extension Option
            elif self.option == "Extension Option":
                if self.duration < (0.4 * self.useful_life) or self.duration > (0.9 * self.useful_life):
                    if self.ext_rate < self.market_rate:
                        output = "The lease is a finance lease and the asset is to be capitalised with the Lessee"
                        # global l
                        l = 1
                        return output
                    else:
                        output = "The lease is a finance lease and the asset is to be capitalised with the Lessee"
                        # global l
                        l = 1
                        return output

                elif (0.4 * self.useful_life) < self.duration < (0.9 * self.useful_life):
                    if self.ext_rate < self.market_rate:
                        output = "The lease is a finance lease and the asset is to be capitalised with the Lessee"
                        # global l
                        l = 1
                        return output
                    else:
                        output = "The lease is a finance lease and the asset is to be capitalised with the Lessor"
                        # global l
                        l = 2
                        return output

            elif self.option == "Special Leasing":
                output = "The asset is a special lease and is generally capitalised with the Lessee"
                # global l
                l = 1
                return output
            else:
                output = "Invalid options provided"
                return output

    ################################################## Accounting Entries



    def journals(self,
                 cost,
                 monthly_rate,
                 duration,
                 pen_can,
                 option,
                 useful_life,
                 purchase_price,
                 net_book_value,
                 ext_rate,
                 market_rate,
                 interest):

        if l == 0 or l == 2:

            depn = round(self.cost / self.useful_life)

            second_output = (f"The lessee will post the leasing rate on a monthly basis to operating expenses as follows\n"
                             f"Dr Operating Expenses (P/L) {self.monthly_rate}\n "
                             f"Cr Bank or Accounts Payable (BS) {self.monthly_rate} \n"
                             f"The lessor will capitalise the asset on his balance sheet an amortise it according to its useful life as follows\n"
                             f"Debit Fixed Assets (BS) {self.cost}\n "
                             f"Debit Depreciation (P/L) {depn}\n "
                             f"Credit Bank or Accounts Payable (BS) {self.cost}\n "
                             f"Credit Accumulated Depreciation (BS) {depn}")
            return second_output

        elif l == 1:

            total_payments = self.monthly_rate*self.duration
            depreciation = round(total_payments/ self.useful_life)
            years = int(self.duration/12)
            interest_charges = []
            opening_balances = [self.cost]
            lease_creditor_reductions = []
            closing_balances = []
            initial_text = (f"**The asset is to be capitalised with the lessee as follows:**\n\n"
                            f"    Dr Fixed Assets (BS) {total_payments}\n\n"
                            f"    Cr Lease Creditor (BS) {total_payments}\n\n"
                            f"    Being capitalisation of the asset with the lessee\n\n"
                            f" **The journal entries for the subsequent years are:**\n\n ")
            updated_text = initial_text

            for i in range(years):

                interest_charge = round(opening_balances[i]*self.interest)
                interest_charges.append(interest_charge)
                lease_creditor_reduction = (self.monthly_rate*12) - interest_charge
                lease_creditor_reductions.append(lease_creditor_reduction)
                calculation = opening_balances[i]-lease_creditor_reductions[i]
                opening_balances.append(calculation)
                closing_balances.append(calculation)

                subsequent_text = (f" **For the lessee in year {[i]}**:\n\n"
                                   f"    Dr Interest expense (P/L) {interest_charges[i]}\n\n"
                                   f"    Dr Lease creditor (BS) {lease_creditor_reductions[i]}\n\n"
                                   f"    Cr Bank (BS) {self.monthly_rate*12}\n\n"
                                   f"    Being amortisation of the lease liability for the lessee \n\n"
                                   f"\n\n"
                                   f"    Dr Depreciation (P/L) {depreciation}\n\n"
                                   f"    Cr Accumulated Depreciation (BS) {depreciation}\n\n"
                                   f"    Being yearly depreciation for the asset\n\n"
                                   f"The opening balance for year {[i]} is {opening_balances[i]}\n\n"
                                   f"The closing balance for year {[i]} is {closing_balances[i]}\n\n"
                                   f"\n\n"
                                   f"**For the Lessor in year {[i]}:**\n\n"
                                   f"    Dr Accounts Receivable (BS) {self.monthly_rate*12}\n\n"
                                   f"    Cr Revenue (P/L) {lease_creditor_reductions[i]}\n\n"
                                   f"    Cr Interest income (P/L) {interest_charges[i]}\n\n"
                                   f"    Being lease revenue recognition \n\n"
                                   f"*Once monies has been received:*\n\n"
                                   f"    Dr Bank (BS) {self.monthly_rate*12}\n\n"
                                   f"    Cr Accounts Receivable (BS) {self.monthly_rate*12}\n\n"
                                   f"    Being receipt of payment for receivable\n\n")

                updated_text = updated_text + subsequent_text

            return updated_text

        else:

            third_output = ("Insufficient information for conclusion. Please review.")

            return third_output



