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
The goal of this project is to create a data-driven decision making tool to enable real-estate development business owners to make the optimal decision for acquiring heavy equipment such as bulldozers and tractors. Given the high cost of such equiptment, it is important to make a decision that is not only cost effective, but also of low risk. This paper describes a decision analysis tool that augments a classic rent vs finance vs buy analysis for a given piece of heavy equiptment with a prediction tool that predicts the chance of catastrophic failure during the time periods of use. 

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
We define the state space $\ X$ as the set of possible outcomes. In the case of our decision tool $\chi_{tn}$ is the operational state of the machine within a period of work hours p. For example, $\chi_{p1}$ is the operational state of a bulldozer within the first 1000 work hours in which the operational state is either operational or not operational.

Let $\chi_{p1}$, $\chi_{p2}$ ,..., $\chi_{pn} \in \ X$

Where:

\begin{table}[h!]
\centering
\begin{tabular}{ll}
\hline
State Space &                 \\ \hline
$\chi_{pn}$ & Operational     \\
$\chi_{pn}$ & Not Operational
\end{tabular}
\caption{Set of states}
\label{state-space}
\end{table}





# Predictive Model


# Value


# Methodology

## Data Generation

# Example

# Results

# Conclusions

# Future Work

In future work this project can be built out into a web tool with an inuitive interface. If expanded in this way, it could grow into a software product that could be sold to companies. A better data set collected from bulldozer repair operations could further improve our tool to provide more accurate predictions.

# Acknowledgements

I would like to acknowledge Dr. Arthur Small for teaching this wonderful class and providing helpful feedback for the project. I would also like to thank Robbie Dickinson for his helpful insights in the heavy equipment industry. Finally, I would like to thank my friends in the real-estate industry for providing insight from the perspective of a real-estate stakeholder.

# References
[1] “Bulldozers Purchasing Guide,” Purchasing.com. [Online]. Available: https://www.purchasing.com/construction-equipment/bulldozers/purchasing-guide/index.html. [Accessed: 26-Apr-2020].

[2] R. Misheloff, “How Much Does It Cost to Finance or Lease a Bulldozer?,” Equipment Leasing and Small Business Loans with Smarter Finance USA. [Online]. Available: https://www.smarterfinanceusa.com/blog/bulldozer-financing-leasing. [Accessed: 26-Apr-2020].