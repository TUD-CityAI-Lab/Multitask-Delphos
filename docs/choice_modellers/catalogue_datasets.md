---
hide:
  - toc
---

# Understanding Catalogue Datasets

Delphos includes a collection of discrete choice datasets in its Catalogue. Each dataset defines a model specification problem which is used for either training or evaluating Delphos performance on that task. In this tutorial, we explain:

1. What a task is.
2. How tasks are represented internally.
3. How the catalogue is constructed.
4. How to inspect catalogue datasets.

## What is a Task?

In Delphos, a Task describes a discrete choice model specification problem given a dataset and modelling choices.

A task contains:

- The dataset on which the model is estimated.
- The choice set available to decision-makers.
- The attributes that describe those alternatives.
- The socio-demographic variables used to capture taste heterogeneity.
- The transformations that may be applied to attributes (e.g. linear, log, box-cox).
- The taste structures that may be considered for parameters (e.g. generic, specific).

Conceptually, a task defines the **modelling space** that Delphos is allowed to explore. For example, the Swissmetro task contains:

- Alternatives: Car, Rail, Swissmetro.
- Attributes: Travel Time, Travel Cost, Headway, Seat Availability.
- Covariates: Income, Purpose, etc.
- Transformations: Linear, Log, Box-Cox.
- Taste structures: Generic and Alternative-Specific.

## Working with Tasks

!!! example "Step 1: Load a Catalogue dataset"

Catalogue datasets can be loaded directly using their name.

```python
from delphos import Delphos
task = Delphos.load_dataset("swissmetro")
```

Inspect the task:

```python
print(task)
```

Example output:

```python
Task(name='swissmetro', alternatives=3, attributes=7, covariates=4)
```

!!! example "Step 2: Inspect alternatives"

Alternatives represent the available choice options for decision-makers. In the Swissmetro dataset, the alternatives are:

```python
task.alternative_names

# Example output:
('car', 'rail', 'swissmetro')
```

You can also inspect the full alternative objects:

```python
task.alternatives
```

Example output:

```python
(   Alternative(
        id=1,
        name="car",
        choice=1,
        availability="av_car"
    ),
    Alternative(
        id=2,
        name="rail",
        choice=2,
        availability="av_rail"
    ),
    Alternative(
        id=3,
        name="swissmetro",
        choice=3,
        availability="av_swissmetro"
    )
)
```

!!! example "Step 3: Inspecting attributes"

Attributes define the explanatory variables available for modelling.

```python
task.attribute_names
```

Example output:

```python
('travel_time', 'travel_cost', 'headway', 'seat_availability')
```

To inspect a particular attribute:

```python
task.get_attribute("travel_time")
```

Example output:

```python
Attribute(
    id=2,
    name='travel_time',
    alternative={ 1: 'car_tt', 2: 'rail_tt', 3: 'sm_tt' }
)
```

This mapping indicates which dataset column corresponds to the travel time attribute for each alternative.

!!! example "Step 4: Inspecting covariates"

Covariates are variables that can be used to model systematic taste heterogeneity. The levels attribute indicates the categories available for that covariate.

```python
task.covariate_names
```

Example output:

```python
('income', 'purpose', 'gender')
```

Inspect a specific covariate:

```python
task.get_covariate("income")
```

Example output:

```python
Covariate( id=1, name='income', levels=(0, 1, 2) )
```

!!! example "Step 5: Inspecting transformations"

Delphos currently supports three non-linear transformations that can be applied to attributes to explore different functional forms.

```python
task.transform_names
```

Output:

```python
('linear', 'log', 'box_cox')
```

!!! example "Step 6: Inspecting taste structures"

Delphos currently supports two taste structures: generic and alternative-specific. A generic taste parameter is shared across alternatives, whereas a specific taste parameter is estimated separately for each alternative. Dummy coded attributes can be further included in the grammar.

```python
task.taste_names
```

Output:

```python
('generic', 'specific')
```

## What is the Catalogue?

A Catalogue combines multiple tasks into a common modelling grammar.

Suppose we have three choice modelling datasets: (i) the Swissmetro choice experiment, (ii) London Passenger Mode Choice (LPMC), and (iii) Norway Value of Travel Time. Although these datasets differ, many modelling concepts are shared:

- Travel time, Travel cost, other attributes.
- Income, gender, age, other socio-demographics.
- Conception of transport modes or alternatives.

The Catalogue thus assigns global identifiers to attributes and sociodemographic variables so that they can be represented consistently across tasks. This enables Delphos to learn modelling strategies on one dataset and transfer them to another.

Instead of traditional model specification approaches that are dataset-specific, Delphos uses a global modelling grammar that allows it to learn across multiple datasets and transfer specification knowledge to unseen tasks. For instance, travellers often exhibit a diminishing sensitivity to increases in travel time: the perceived difference between a 10- and 20-minute trip is typically larger than the difference between a 110- and 120-minute trip. If Delphos repeatedly observes that non-linear transformations of travel time improve model performance across several transport datasets, it can learn to prioritise such specifications when analysing a new dataset. In this way, Delphos transfers modelling knowledge rather than transferring parameter values from one dataset to another.

!!! example "Step 7: Inspecting the Catalogue"

The catalogue can be loaded directly:

```python
from delphos import Delphos
catalogue = Delphos.load_catalogue()
```

Inspect the catalogue:

```python
print(catalogue.summary())
```

Example output:

```text
Catalogue( tasks=12, attributes=15, covariates=8, transformations=3, tastes=2 )
```

!!! example "Step 8: Global Modelling Grammar

The catalogue stores the complete set of modelling space parameters that define the search space for Delphos. It uses these global identifiers to represent every model specification.

```python
catalogue.global_attribute_ids

catalogue.global_covariate_ids

catalogue.global_transform_ids

catalogue.global_taste_ids
```

---

## Next Step

Continue to [Using Your Own Datasets](own_datasets.md) to learn how to define new tasks and integrate your own discrete choice datasets into Delphos.
