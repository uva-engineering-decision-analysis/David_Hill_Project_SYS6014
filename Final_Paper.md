---
title: Optimizing the Aquisition of Heavy Equipment for Small Businesses
subtitle: Project for University of Virginia SYS 6014 Decision Analysis Spring 2020
author: David Hill, Jr. (dh5dn@virginia.edu)
papersize:
- a4
fontsize:
- 12pt
geometry:
- margin=1in
fontfamily:
- charter
header-includes:
- \setlength\parindent{24pt}
- \usepackage{placeins}
---

\maketitle
\pagenumbering{arabic}
\setcounter{page}{1}

# Abstract
**The goal of this project is to create a data-driven decision making tool to enable real-estate development business owners to make the optimal decision for acquiring heavy equipment such as bulldozers and tractors. Given the high cost of such equiptment, it is important to make a decision that is not only cost effective, but also of low risk. This paper describes a decision analysis tool that augments a classic rent vs finance vs buy analysis for a given piece of heavy equiptment with a prediction tool that predicts the chance of catastrophic failure during the time periods of use.** 

# Introduction
The real-estate industry, being one of the oldest in our economy is ripe for a digital transformation. With new technologies being rapidly developed to provide data driven insights every day, it is imperative that new tools be developed for the real-estate industry as well. For small to medium-sized real-estate development businesses the acquisition of tools and equipment is key to generating, and maintaining business as these tools enable the completion of projects. Generally, the acquisition decisions for heavy equipment (such as bulldozers and tractors) are done by the owners or stakeholders of the businesses. These decisions are often made with limited financial resources, which makes good decision making very important. Poor acquisition decisions can be very crippling to a small business as it can lead to personnel injury, and loss of capital due to equiptment failure.

During an interview conducted with Robbie Dickinson, Owner of Kubota Dealership Dickinson Equipment Inc. in Fredericskburg, VA, stated that buyers of heavy equipment such as tractors and bulldozers make their decision based on consultation with him or his sales people. He also stated that most of his customers come with a preconceived notion of whether they want to buy, finance, or lease a piece of equipment. Moreover, he explained that older aged customers often prefer to purchase equiptment outright while younger customers prefer to finance. In the interview with him, it was clear that there is a need for a data-driven decision tool to help make the optimal acquisition decision based on customers' needs. 

In this paper, I will introduce a novel decision analysis tool that will enable owners and stakeholders of small to medium-sized real-estate development companies to make the optimal acquisition decision given the financial posture, risk tolerance, and organizational goals. The tool operates as two separate parts. The first part is a classic rent versus buy analysis that takes into consideration the decision makers' goals. The second part uses failure data to calculate the chance that the piece of equiptment will fail within periods of work-hours. This paper will mainly focus on the acquisition of a bulldozer for land development but the same methodology can be extended and used for other types of equipment such as cranes and fork lifts.

# Background
Modern Bulldozers have come a long way since their creation in the early 1900's. "Now incorporating a wide range of automated monitoring features, hydraulic systems, and ergonomic joystick controls, they are capable of productivity unimaginable just a few decades ago [1]." In most cases, bulldozers are classified in 3 main sizes: small, medium and large [1]. They are even further categorized by power output (horsepower), weight class, and blade size [1]. 

## Purchasing Considerations
The leading manufacturers for bulldozers globally are John Deere, Caterpillar, Komatsu, Liebherr and Bobcat. These manufacturers produce two main types of bulldozers: crawlers (which operate on tracks) and wheel based (equipped with heavy-duty, all-terrain tires like those found on a rough terrain forklift) [1]. "Crawler bulldozers are far more prevalent than their wheeled counterpart. In fact, a quick analysis of the total number of models available on the market - both new and used - reveals a split of 105:1 in favor of the track-based crawler design [1]." 

## Benefits
Bulldozers are multi-purpose vehicles that are pivotal to both private and government operations. This is due to their primary attachments: the blade and the ripper [1]. Bulldozers greatly improve the efficiency of projects that would otherwise require hours of manual labor. The tasks that can be completed by a bulldozer are as follows:

* Backfilling
* Snow removal
* Sweeping
* Grading 
* Ditching 
* Stump removal
* Loading
* Demolition
* Excavating

## Trends
One of a businesses main goals is to reduce it's costs to maintain or create a competitive edge. For real-estate development companies this can be achieved by purchasing used equiptment. "A recently manufactured used bulldozer provides much of the same technology for 30% to 70% less than the price of a comparable new machine [1]". Given this, there are still pros and cons to acquiring a new versus a used bulldozer.

### New Bulldozers

#### Pros
* Latest Technology - Newer technology translates to improved fuel efficiency, better telemetry systems, better emissions, improved cab design. These improvements can make the machine more comfortable and easy to operate thus, increasing productivity, lowering the cost of ownership while making them more cost-effective on every job [1].

* Customizable - A new bulldozer can be built with specific modifications that meet an endless variety of specifications [1]. In this way, a new machine may be more productive as it's been designed for a specific application. This includes both the mechanical features as well as specific attachments [1].

* Warranty - A new bulldozer is typically backed by at least a one-year warranty, with optional coverage provided direct through the manufacturer that can extend the initial warranty up to three years or 10,000 hours (monthly fee/deduction applies) [1]. This coverage travels with the machine wherever it's in operation [1].

* Low Failure Risk - A new bulldozer will have virtually no work hours on it and have all new parts with no wear. Thus making it unlikely that it will have an expensive failure in the near future.

#### Cons
* Expensive - A new bulldozer represents a serious investment. Looking at a new mid-range model, one that offers 335 hp, you can expect to pay $180,000 to $340,000 depending on the brand and any additional customizations [1]. This outlay is not viable for many small to mid-range businesses without financing and may even represent more of a financial risk for this type of buyer in the event of economic fluctuation [1].

* Hidden Costs - A new bulldozer may have hidden costs such as full coverage insurance if financed and a fixed or variable interest rate depending on the lender.

### Used Bulldozers

#### Pros
* Much Less Expensive - On average, a used bulldozer can be found for 30% to 70% less than a new machine [1]. 

* Generally Reliable - Bulldozers are built to withstand extreme operation for decades [1]. While each individual application will dictate the machine's ultimate longevity, they're reliable for at least 10,000 hours without any major repairs - and some a lot longer with proper service and maintenance [1]. This lifespan enables a potientially solid return on the initial investment. 

#### Cons
* Older Technology - Used bulldozers are available with production dates going back to the 1970s. Models older than 10 years old may not offer the same conveniences as a newer machine which may pose a problem to operator that are used to the modern technology [1]. An older machine may not get a comparable level of fuel efficiency due to the improvements recently made to diesel engines, thus increasing the cost of operation in comparison to a newer machine [1].

* Higher Failure Risk - An older machine poses a higer risk of having worn parts that may fail shortly after acquiring it. It is also very difficult to determine the maintainence history of the bulldozer which can increase the cost of ownership with hidden maintainence costs. 


# Decision Problem
The decision problem that the business owner must overcome is a whether or not buying, renting, or financing a bulldozer or piece of equipment makes sense under different economic scenarios. Additionally, if aquiring a used piece of equiptment makes the most sense, what is the risk of catastropic failure withing different time dimensions. The formal definition of the decision problem is as follows:

## Action Space
We define the decision maker's action set $\ A$ as the set of actions the user can make within our decision tool.

Let $\alpha_{1}$, $\alpha_{2}$ ,..., $\alpha_{n} \in \ A$

Where:

\begin{table}[!h]
\centering
\begin{tabular}{ll}
\hline
Action Set   &                             \\ \hline
$\alpha_{1}$ & Buy new outright  \\
$\alpha_{2}$ & Finance new       \\
$\alpha_{3}$ & Rent used         \\
$\alpha_{4}$ & Buy used outright \\
$\alpha_{5}$ & Finance used      \\ \hline
\end{tabular}
\caption{Users Action Set}
\label{tab:my-table}
\end{table}


## State Space
We define the state space $\ X$ as the set of possible outcomes. In the case of this project we assume that under average construction conditions a bulldozer will work for 1,584 hours. This is derived by the following:

$22 working days/month  *  9 working months * 8 hours/day = 1584 hours/year$

To account for discrete periods of work hours we let:

$\chi_{1}$, $\chi_{2}$ ,..., $\chi_{n} \in \ X$

Where $\chi$ is the number of expected failures in a period of 1584 work hours. For the purposes of our tool $\chi =1$ because we expect exactly 1 failure to happen within given work hour periods.

\begin{table}[h!]
\centering
\begin{tabular}{ll}
\hline
Parameter Space            &                                                                       \\ \hline
\multicolumn{1}{c}{$\chi_{n}$} & \multicolumn{1}{c}{Number of expected failures per  work hour period}
\end{tabular}
\caption{Set of states}
\label{state-space}
\end{table}

## Parameter Space
Our unobserved parameter is a function of lambda. Hence $\theta$ is the calculated chance of exactly one mechanical failure will happen within a give time period. Here we let:

$\theta_{1}$, $\theta_{2}$ ,..., $\theta_{n} \in \Theta$

\begin{table}[h!]
\centering
\begin{tabular}{ll}
\hline
Parameter Space              &                                                         \\ \hline
\multicolumn{1}{c}{$\theta_{n}$} & \multicolumn{1}{c}{Probability of catastrophic failure}
\end{tabular}
\caption{Set of unobserved parameters}
\label{state-space}
\end{table}

# Assumptions
If there is one thing i have learned through my studies of Engineering, it is that educated assumptions are okay as long as they are stated, thus the purpose of this section is to address built-in assumptions in the decision tool. Seeing as this tool is designed for the targeted audience of stakeholders in small-medium sized real-estate development companies, the assumptions reflect the needs of that audience. The assumptions are as follows:

* The predictive decision tool assumes that the failure data passed in contains a set of used bulldozers that failed after a 1584 work hour period. 

* The tool also assumes that the failure rate of a bulldozer is based on similar bulldozers within the range of 500 work hours higher or lower than the actual bulldozer. For example, if a bulldozer with 1500 work hours is specified, it will be grouped with bulldozers with work hours between 1000 and 2000 to determine the failure rate.

* It is also assumed that failure rate is based on a grouping of a certain type of bulldozer over the entire data set. For example if a dataset with a total of 10000 bulldozers has 5000 failed bulldozers with work hours between 1000 and 2000, then the failure rate of bulldozers in the range of 1000 and 2000 work hours is: $\frac{5000}{10000} = .05$

* The failures follow a Poisson distribution as we want to find the probability of exactly one failure happening in a period of work hours.

# Predictive Model

## Distribution
The statistical distribution used for our decision tool is the poisson distribution. After evaluating the geometric and negative binomial distributions, it seemed most natural to use the poisson distribution and consider the failure rate that determines our $\lambda$ in terms of work hour periods.

### Poisson Distribution
The Poisson Distribution expresses the probability of a given number of events occurring in a fixed interval of time or space if these events occur with a known constant mean rate and independently of the time since the last event.

A discrete random variable $\chi$ is said to have a Poisson distribution with parameter $\lambda$ > 0, if, for $\chi$ = 0, 1, 2, ..., the probability mass function of $\chi$ is given by:

$P(\chi = \ X) = \frac{\lambda^{\chi} \times e^{-\lambda}}{\chi !}$

where:

$\mu = \lambda$

$\sigma^{2} = \lambda$

$e = 2.71828...$

> Note: $\chi$ will represent the number of expected occurances of an event happening in a time period (e.g. the probability that $\chi =4$ car accidents will happen in 3 weeks when the rate of car accidents is 1.5 per week

# Value
The underlying value of our decision tool is it's ability to reduce uncertainty for the decision maker. It enables them to make the most sound financial decision and also be informed as to what to expect in terms of reliability. With this tool, a decision maker can weigh the failure risks and financial risks in a way that is supported by market based data. Given this, our payoff is defined as a function of the financial benefit to the decision maker and the risk of the worst case scenario. The payoff function is defined as follows:

$Payoff = NPV + Risk$

Where NPV is the net present value of the optimal acquisition decision and Risk is the financial impact of the risk of failure.

# Methodology
The methodology to this project is two-fold. The first part is a Rent v.s Buy analysis that allows the user to input equipment rental and purchasing scenarios underdifferent cashflow assumptions. 

## Rent v.s Buy Analysis
For the rent v.s buy analysis there are a few essential calculations that must be highlighted. This part of the tool calculates payment costs over desired time periods as well as Net Present Value (NPV) and Facilities Capital Cost of Money (FCCM). FCCM is defined in the US Army Corps of Engineers Construction Equipment Ownership and Operating Expense Schedule for Region II which includes the state of Virginia. 

The pivotal formulae defined in this expense schedule are as follows:

$OwnershipRate/hr = DEPR/hr + FCCM/hr$ [3]

DEPR - Depreciation as the straight-line method is used to compute depreciation [3].

$DEPR/hr= \frac{[(TEV)(1-SLV)]-[(TCI)(TireCost)]}{LIFE}$ [3] 

Where:

TEV is the total equipment value found in table 2-1 [3]

SLV is the salvage value from appendix D. [3]

TCI is the tire cost index, which is determined by dividing the year of
manufacture tire index by the present-year tire index. For table 2-1, the present year is
2018 and the year of manufacture is 2015 (3 years old). These indices are listed as
part of appendix E (see Economic Key (EK) 100, All Tires and Tubes). [3]

Tire cost is the total tire and/or conveyor belt cost. The total tire cost is the
sum of the cost of all front, drive, and trailing tires. The tire cost for rubber-tired
equipment is based on tire values at the time the equipment was manufactured. [3]

The LIFE is the economic life, which is based on the number of operating hours
throughout the economic life of the equipment (see paragraph 2.15). Hours for LIFE are
provided in appendix D. [3]

$FCCM/hr= \frac{(TEV)(AVF)(DiscountedCMR)}{WHPY}$ [3]

Where:

$AverageValueFactor(AVF)= \frac{[[(N - 1)(1+ SLV)]+ 2]}{2N}$ [3]

Number of Years (N) in Depreciation Period = $\frac{LIFE}{WHPY}$ [3]

Discounted CMR = 3.500% (Jul – Dec 2018 rate) / 1.25 = 2.80%. [3]

WHPY = Working hours Per Year found in appendix B [3]

## Failure Risk Analysis
This goal of this part of the decision tool is to predict the probability of failure of a bulldozer or piece of equipment that makes the most financial sense. This tool should be run after the rent v.s buy analysis is conducted. This tool starts by asking the decision maker a series of questions. Based on the parameters collected from the decision maker, the tool compares the parameters to market-driven, generated bulldozer data to determine the failure rate of a machine that matches those parameters. It then calculates the lambda values and poisson probabalities for failure over the period of ownership and period in which failure is acceptable per the user's specification. 

## Data
The data generation process for this project involved 3 distinct parts; web-scraping, cleaning, and data generation. After much research and advice from industry, it was clear during the research that there are almost no datasets that show bulldozer failures. The data that is available through used bulldozer listing sites is censored data in the sense that the only bulldozers being represented are working ones. Given these constraints, it was natural to use market data from working bulldozers to generate artificial datasets to base predictions on. 

# Example

# Results

# Conclusions

# Future Work
In future work this project can be built out into a web tool with an inuitive interface. If expanded in this way, it could grow into a software product that could be sold to companies. A better data set collected from bulldozer repair operations could further improve our tool to provide more accurate predictions. Furthermore, our data generation could be improved through a deeper cleaning in which anomalous entries are removed (such as an 20 year old bulldozer with low  work-hours). The ability to pull bulldozer data from multiple sources would also provide more accurate predictions as well.

# Acknowledgements

I would like to acknowledge Dr. Arthur Small for teaching this wonderful class and providing helpful feedback for the project. I would also like to thank Robbie Dickinson for his helpful insights in the heavy equipment industry. Finally, I would like to thank my friends in the real-estate industry for providing insight from the perspective of a real-estate stakeholder.

# References
[1] “Bulldozers Purchasing Guide,” Purchasing.com. [Online]. Available: https://www.purchasing.com/construction-equipment/bulldozers/purchasing-guide/index.html. [Accessed: 26-Apr-2020].

[2] R. Misheloff, “How Much Does It Cost to Finance or Lease a Bulldozer?,” Equipment Leasing and Small Business Loans with Smarter Finance USA. [Online]. Available: https://www.smarterfinanceusa.com/blog/bulldozer-financing-leasing. [Accessed: 26-Apr-2020].

[3] USACE