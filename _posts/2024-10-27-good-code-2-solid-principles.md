---
layout: post
title: Writing good code 2 - the SOLID principles applied to scientific code
date: 2024-10-27 15:09:00
description: A discussion of the most important paradigms of professional software development and how they can help us write good code in science.
tags: code
categories: code
featured: false
---

In my post about [variable naming and function extraction]({% post_url 2024-07-20-good-code-1-proper-naming-in-scientific-code %}) I tried to convey how simple it is to make code readable and understandable.

Tthere are a few other software development paradigms and principles that aid in creating such
understandable, but also maintainable, extendable, and testable code. Five core
principles for object-oriented software design have been developed by
Robert Martin and later termed by the acronym SOLID by Michael Feathers (Martin, 2000). These principles
have been developed for agile software development where adaptations and
new features have to be implemented in fast iterations. This is obviously
not usually the case in scientific modeling. Nevertheless, they can be
helpful also for scientific code because they help in making code more
testable and maintainable, which is why I want to explain them here.

# The SOLID principles of object-oriented programming languages

The five SOLID principles are the following:

1. The **S**ingle responsibilty principle states that classes (or functions) should be responsible for one thing only. This allows clear distinction of what is done where.
2. The **O**pen-closed principle constitutes that code should be open for extension (allowing new functionality) but closed to modification (the extension should not require modification of the existing code).
3. The **L**iskov substitution principle formalizes proper usage of inheritance.
4. The **I**nterface segregation principle defines that the interfaces between modules should be kept as small as possible to restrict unnecessary access, thereby limiting room for erronous behavior.
5. The **D**ependency inversion principle states how to deal with modules depending on one another and how to handle dependencies for better testability.

By the way, although they were developed for object-oriented programming, the SOLID principles are also applicable (in adapted form) to functional programming (see, e.g., Kocik (2022)).

Here they are in more detail:

## 1. Single responsibility principle

Extracting well-named functions can be helpful to make
code more understandable, maintainable, and testable. This is achieved
best when these functions are not overloaded but ideally do **one
particular thing only**. This idea is called the _single
responsibility principle_. The principle was introduced for classes but holds for functions as well. A class that computes the radiation budget at the Earth's surface should not also compute the water budget. These two things are of course heavily
related, but should be split up if possible.

Look at the following example code snippet adapted from the dynamic vegetation model LPJ-GUESS (Smith et al., 2014). All logic is divided into
multiple functions that get called one after the other. This is a good
example of the single responsibility principle where each function deals
with one thing.

{% highlight c++ linenos %}
void simulateDay() {
...
leafPhenology(patch, climate);
interception(patch, climate);
initialInfiltration(patch, climate);
canopyGasExchange(patch, climate);
irrigation(patch);
soilwater(patch, climate);
...
}
{% endhighlight %}

<div class="caption">
    This example code adapted from the dynamic vegetation model LPJ-GUESS nicely extracts code into different functions with clear names that are responsible for one thing.
</div>

## 2. Open-closed principle

Code should be open for extension, but closed for modification. This
means, that the class itself should be able to deal with new
requirements without changing anything within that class.

Consider the following example adapted from LPJ-GUESS computing leaf phenology. The code is technically not open for extension. If a new plant lifeform is added, we need to modify this code and add another `if`.

{% highlight c++ linenos %}
void leafPhenology(Plant plant, Climate climate){
// ...
double phenology = 1.0;
if (plant.lifeform == TREE){
phenology = min(1.0, (climate.gdd5 - plant.gdd0[climate.chilldays]) / pft.phengdd5ramp);
} else if (plant.lifeform == GRASS) {  
 phenology = min(1.0, climate.gdd5 / plant.phengdd5ramp);
}
// ...
}
{% endhighlight %}

<div class="caption">This code violates the open-closed principle.</div>

Here, it could be better to make use of inheritance in object-oriented languages. One could introduce classes `Tree` and `Grass` that implement an interface (or extend an abstract class) `Plant` that has a method `phenology()`.
Then, we can call `plant.phenology()` directly without having to check its type again. And adding a new type of plant would not change any code in the adapted snippet below. The new plant would implement their own `phenology()` function:

{% highlight c++ linenos %}

void leafPhenology(Plant plant, Climate climate){
// ...
double phenology = plant.phenology(climate);
// ...
}

public interface Plant {
public double phenology(Climate climate);
}

public class Tree extends Plant {
public double phenology(Climate climate){
return min(1.0, (climate.gdd5 - gdd0[climate.chilldays]) / phengdd5ramp);
}
}

public class Grass extends Plant {
public double phenology(Climate climate){
return min(1.0, climate.gdd5 / phengdd5ramp);
}
}

{% endhighlight %}

<div class="caption">
	This example is open for extension and closed for modification. The function `leafPhenology` will not need to be adapted if a new type of plant is introduced.</div>

This way of organizing the code is more maintainable, because we do not need to touch `leafPhenology` again if we want to change the behavior of `Tree`s or `Grass`es or add a new type of `Plant`.
It needs to be noted, however, that for a single such situation it is probably not worth designing a new class hierarchy. Creating a class hierarchy needs to be well thought out, because it will be hard to change later. However, if you find yourself having to write similar if-else-statements around the model code, creating a class abstraction is probably sensible.

## 3. Liskov substitution principle

A benefit of object-oriented programming is the concept of inheritance,
where a subclass is derived from a superclass to extend the behavior of
that superclass. We have seen this above already in the Open-close principle.

The introduced `Plant` interface (it could also be a class) will have sub-types like `Tree`, which will in turn have other subtypes, for instance
`NeedleleavedTree` and `BroadleavedTree`. In this
regard, the Liskov substitution principle is the principle guaranteeing
that no inconsistent behavior happens when creating such a hierarchy. It
states that if class A is a subtype of B, we should be able to use
objects of type A and B interchangeably without breaking the behavior of
the model.

Basically this boils down to designing a proper inheritance hierarchy.
An example violating this rule is found below.

{% highlight c++ linenos %}
class BroadleavedTree {
void leafOut(){
// grow broad leaves
}
void senescence(){
// drop leaves in autumn
}
}
class CommonOak extends BroadleavedTree { ... }
class HolmOak extends BroadleavedTree { ... }

{% endhighlight %}

<div class="caption">
The problem here is that unlike most broad-leaved trees, a holm oak actually is also an evergreen tree and does not drop its leaves. The class hierarchy is therefore not ideal.
</div>

In general it is simply important to keep in mind that class types need
to be interchangeable when designing the hierarchy (e.g., a class
`Bird` would probably have a method `fly()`, but then there
are birds that don't fly). There are numerous ways to fix a violation of
the principle, for instance redesigning the class hierarchy or not using
inheritance where we don't need to (this is also called
**composition over inheritance**).

In the given example, the method `senescence()` could be
extracted from the class `BroadleavedTree` into an interface
`Summergreen`, because this method is not really tied to the characteristic of a tree having broad leaves. This would allow creating various broad-leaved
trees that can drop their leaves or not, depending on whether the interface is implemented or not, like so:

{% highlight c++ linenos %}
class BroadleavedTree {
void leafOut(){
// grow broad leaves
}
}

interface Summergreen {
void senescence(){ ... }
}

class CommonOak extends BroadleavedTree implements Summergreen { ... }
class HolmOak extends BroadleavedTree { ... }
{% endhighlight %}

<div class="caption">
Extracting the senescence function into an interface makes the class hierarchy correct again..
</div>

## 4. Interface segregation

We've seen above already how interfaces can be helpful to hide away logic from other parts of the code (see the example of the Open-closed principle).

There is one additional golden rule about creating such interfaeces:
Instead of creating one large interface it is advisable to create
multiple small ones. Then at another point in the software, only the
``small'' interface is addressed, providing only what is relevant at
this point. Note that interfaces do not exist in all programming
languages, but they can often be emulated by other features of those
languages.

{% highlight c++ linenos %}
public interface Plant{
takeUpWater();
phenology();
doPhotosynthesis();
respire();
grow();
die();
harvest();
sow();
irrigate();
}

public class Cropland {
public void prepareField(Plant plant){
// calling functions like plant.doPhotosynthesis() or plant.respire()
// would be possible here. But is this reasonable?
}
}
{% endhighlight %}

<div class="caption">
Example of a potentially too large interface. The `Cropland` class should not be able to deal with low-level aspects of a `Plant`.
</div>

Every part of the code receiving a `Plant` now can do anything
with that object. According to _interface segregation_, we should
hide unneeded details. In this example, it would make sense to extract
at least one other interface:

{% highlight c++ linenos %}
public interface Plant{
takeUpWater();
phenology();
doPhotosynthesis();
respire();
grow();
die();
}

public interface ManageablePlant{
harvest();
sow();
irrigate();
}

public class Cropland {
public void prepareField(ManageablePlant plant){
// plant.doPhotosynthesis() or plant.respire() can not be called here
// only methods of ManageablePlant (i.e., methods relevant to land use) can be
// called here, e.g., plant.sow() or plant.harvest()
}
}
{% endhighlight %}

<div class="caption">
An example of a segregation of the interfaces of the previous code snippet. In a land use component, only the functions of `ManageablePlant` should be visible.
</div>

In a land use component of an earth system model, we then only need to
pass the `ManageablePlant` and we can be sure that only the
functions of that interface are called. The land use component will not
be able to mess with other aspects which it is not responsible for,
because these are hidden. For instance, `doPhotosynthesis` should
probably not be called from any land use parts of the model and is
therefore not part of the interface `ManageablePlant`.

In a programming language without interfaces, similar results may be
achieved through other means, for instance virtual methods and abstract
classes.

## 5. Dependency inversion

This principle aims at decoupling modules from one another. High level logic should not depend on a particular implementation at a low level. In regular
software this is essential to switch out modules easily, e.g. replace a data source.

This is probably not a crucial thing in scientific code and models. However, there is one critical benefit of
this principle: It makes the code more testable, because we can plug in
and test things easily because you can
pass things directly.
A negative example is shown in the following code snippet. The `simulateClimateProjection`-function is hard to test, because we cannot easily test what happens under various climates.

{% highlight c++ linenos %}
public class Gridcell{
private Climate climate;
public Gridcell(){
this.climate = readClimateFromFile();
}
void simulateClimateProjection(){
double temperature = climate.getTemperature();
...
}
}
{% endhighlight %}

<div class="caption">
This code violates the dependency inversion principle. The high level class `Gridcell` depends on the implementation of `Climate`.
</div>

An improved implementation is achieved by passing the climate through the constructor. In a testing environment, various climate objects can be created and passed.

{% highlight c++ linenos %}
public class Gridcell{
private Climate climate;
public Gridcell(Climate climate){
this.climate = climate;
}
void simulateClimateProjection(){
double temperature = climate.getTemperature();
...
}
}
{% endhighlight %}

<div class="caption">
In this example, the dependency of `Gridcell` on `Climate` is being injected. `Gridcell` does not have to create the `Climate` itself because it is *injected*. This makes it easier to test: In a unit test, we can pass different climates and call `simulateClimateProjection()`.
</div>

When testing the code, we can now simply insert our own `Climate`
when creating a `Gridcell` and easily test what happens when we
run `simulateClimateProjection` after having passed various climates.

# Conclusion

For a scientist, this was probably quite the deep-dive into topics of software engineering. However, I believe that one needs to simple remember the gist of these SOLID principles:

1. Code portions should have one responsibility and not do hundred things
2. Code should be designed that modifications or extensions need minimal adaptation of code
3. Code that can take different arguments should work for all types of arguments that they allow
4. Internal logic that can be hidden should be hidden
5. Code at a high level should be designed in a way that it is independent from implementations at low levels.

All this also makes code more understandable, maintainable, and testable.

# References

- Kocik, M. (2022). SOLID principles in Functional Programming. [https://medium.com/@mkocik/solid-principles-in-functional-programming-b9b83aeddf80](https://medium.com/@mkocik/solid-principles-in-functional-programming-b9b83aeddf80)
- Martin, R. C. (2000). Design Principles and Design Patterns. Object Mentor. [http://labs.cs.upt.ro/labs/ip2/html/lectures/2/res/Martin-PrinciplesAndPatterns.PDF](http://labs.cs.upt.ro/labs/ip2/html/lectures/2/res/Martin-PrinciplesAndPatterns.PDF)
- Smith, B., Wårlind, D., Arneth, A., Hickler, T., Leadley, P., Siltberg, J., & Zaehle, S. (2014). Implications of incorporating N cycling and N limitations on primary production in an individual-based dynamic vegetation model. Biogeosciences, 11(7), 2027–2054. [https://doi.org/10.5194/bg-11-2027-2014](https://doi.org/10.5194/bg-11-2027-2014)
