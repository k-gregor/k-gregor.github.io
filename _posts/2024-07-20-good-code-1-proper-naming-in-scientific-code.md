---
layout: post
title: Writing good code 1 - Naming, comments, functions, and the DRY principle
date: 2024-10-05 15:09:00
description: Some crucial tips on how to create readable and testable code
tags: code
categories: code
featured: true
---



Scientists are not software developers, yet we often do write software. This could include simple data pre-processing scripts, complex data analyses, or full scientific models.
Here I want to highlight some critical aspects of professional software development and how they could be applied in scientific programming.


## Proper Naming


A trivial yet essential aspect of understandable code is proper naming.
In scientific code, one often comes across variables called `x`, `y`, `xx`, or `ys`. But there is no cost in
using descriptive names such as
`years_since_2000` or `mean_surface_temperatures` which immediately indicate what they contain. Exceptions are known formulas, where the variable names should be as in the formula. For instance,
$$ E=mc^2 $$ does not need to be written as
`energy = mass * light_speed * light_speed`.

Proper variable naming is the number one step to making your code readable and understandable.
Check out the following code. It is simple, yet you have no idea what is going on there:

{% highlight python linenos %}

  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd
  
  a = 0.02
  b = 1
  xx = np.arange(0, 100)
  yy = b*(1+a)**xx
  plt.plot(xx, yy);

{% endhighlight %}

Comments might make this code more understandable. But still, if we use the variable `a` at another point
in the code, we'd have no idea what we're dealing with and have to go back to the declaration to find out:

{% highlight python linenos %}

  a = 0.02 # interest rate
  b = 1 # initial investment
  xx = np.arange(0, 100) # years
  yy = b*(1+a)**xx # money value after x years
  plt.plot(xx, yy);

{% endhighlight %}


With proper variable names, the code is easy to understand:

{% highlight python linenos %}
  interest_rate = 0.02
  initial_investment = 1
  time_years = np.arange(0, 100)
  all_that_money_in_my_bank_account = initial_investment*(1+interest_rate)**time_years
  plt.plot(time_years, all_that_money_in_my_bank_account);
{% endhighlight %}





## Avoid magic numbers

Another trivial, yet often ignored, rule is to avoid "magic numbers". These are numbers in the code that are not explained. For instance, what is going on here?


{% highlight python linenos %}
  time = time * 86400
  emissions = emissions * 44.01/12.011
{% endhighlight %}
<div class="caption">
    It is hard to understand what this code is doing. What to these magic numbers like 44.01 or 86400 mean?
</div>


Instead of writing numbers directly it is much clearer to store the numbers in understandable constants like so:

{% highlight python linenos %}
  SECONDS_PER_DAY = 60 * 60 * 24
  time_days = time_seconds * SECONDS_PER_DAY

  CONVERSION_C_TO_CO2 = 44.01/12.011
  co2_emissions = c_emissions * CONVERSION_C_TO_CO2
{% endhighlight %}
<div class="caption">
	The code is much clearer when magic numbers are extracted into well-named constants.
</div>


## Perks and Pitfalls of comments

Comments are helpful to explain code, as was also shown above. However, it often happens that comments
are outdated because people forget to adapt them when code is changed.
Therefore, proper naming should make the code the first means of
documentation and render additional comments unnecessary.

In scientific models, comments can be used to add citations as to where a formula comes from. Furthermore, comments can be vital in explaining complex parts of the code. However, it needs to be kept in mind that comments are maintained with the rest of the code to avoid
inconsistencies between the two that would lead to confusion.
At the end of the article, there will be an example containing useful commenting.

A final note is that code should never be used **"out-commented"** as this
will only lead to confusion why this code is currently not in use. 
Version control (like `git` or `svn`) allows deleting the code with a commit message explaining why it was deleted.
If it happens that the code is needed again, this commit can be reverted.


{% highlight python linenos %}
  for person in person_list:
      person.calculate_something()

      # person.do_the_thing()
      # person.money = 1000
    
      person.money = 500
      person.do_other_thing()
{% endhighlight %}
<div class="caption">
	My buddy at my old job would call this a "Nonononono!". Other scientists (or you in 1 year!) seeing this code will not understand why we don't to **the thing** anymore, and why the `person` only gets 500 moneys now. Delete the code, write a proper commit message, the change will be easy to understand.
</div>


## The DRY Principle (Don't Repeat Yourself)

Repetition in code is not only a source of clutter, but also a critical
source of errors. If the same piece of code exists in multiple places of
the model and needs changing, chances are that one forgets to change
it in all places. Therefore, such code should be extracted into
well-named functions with well-named parameters that can be called from
anywhere from the model. When the logic needs changing, we only need to
change it in one place. 
This is especially important for other developers who might have to adapt that code. Other than you, they might now know that they need to do the same change in multiple places!
Well-named functions also make the code easier to read, understand, and test. For instance we can easily write a test that checks whether the code from above does what it is supposed to, when this code is extracted into a nice function:

{% highlight python linenos %}
  def calculate_bank_account_value(initial_investment, interest_rate, time_in_years):
    return initial_investment*(1+interest_rate)**time_in_years
{% endhighlight %}


In languages like Python you can even make use of the named function parameters to have a very understandable function call:

{% highlight python linenos %}
  calculate_bank_account_value(initial_investment=1, interest_rate=0.02, time_in_years=8)
{% endhighlight %}

Another benefit is that such functions are easily testable. We'll have another post on that topic soon.

In the case of data processing workflows, things might be a bit different. You might have similar workflows for similar data inputs and the obvious thing is to simply copy the code and adapt it as necessary instead of making it generic. If it is only used once it might also be too much effort to spend lots of time on refactoring it into reusable functions.
Nonetheless, the DRY principle should always be kept in mind. With modern IDEs, extraction of methods is also not a time-consuming task and it helps clarify that the code does what it's supposed to do. This will help when workflows have to be run again, for instance when things pop during the review process of a paper.

Another point where the DRY principle holds in science is when sharing code. Often, someone has a script that they can email to you that will do the data processing you need to do. But this is obviously a way of repeating oneself. Now imagine that you find a bug in the script. How will it be made sure that everyone is informed about the fix? The blog post of Miles McBain (2024) discusses some ideas on how to tackle this.


## A holistic example



Compare the two logically identical implementations of a
zero-dimensional energy balance model below. The first one does the job, but it is quite hard to undestand what's going on, isn't it?




{% highlight python linenos %}
  T = 200 
  # using heat capacity C [J/m^2/K] for 100m deep water as example 
  C = 4.0e+08  
  alpha = 0.3  
  epsilon_earth = 1  
  epsilon_atm = 0.77  
  sigma = 5.67E-8  

  ghe = False  

  TT = []  
  tt = []  

  for t in range(0, 100):  

      T_atm = T/2**(1/4)  
      # compute radiative imbalance by subtracting outgoing
      # longwave from incoming shortwave radiation
      add = (1368*(1-alpha)/4 - epsilon_earth * sigma * pow(T, 4))  
	
      if ghe: # if greenhouse effect should be included
        add += epsilon_atm * sigma * pow(T_atm, 4)  
	
      T += 60*60*24*365*add/C  
      T2 = T - 273.15  

      tt.append(t)  
      TT.append(T2)
{% endhighlight %}
<div class="caption">
	This zero-dimensional energy balance model is hard to understand. Compare this with the same model with extracted functions and proper variable naming in the snippet below.
</div>



In the second snippet, parts of the code are extracted
into well-named functions, magic numbers are stored in constants and
variable names are descriptive. Note also the `if` statement that
previously required an explaining comment which is now replaced by a
speaking variable making the explanation unnecessary. Someone reading
the code will understand it much faster than the first version. These
functions can not only be re-used in other parts of the model, they can
also be easily tested. This contributes to better maintainability and
error-avoidance.



{% highlight python linenos %}
  SIGMA = 5.67E-8 # Stefan-Boltzmann constant [W/m2]  
  SOLAR_RADIATION = 1368 # [W/m2]  
  SECONDS_PER_YEAR = 60*60*24*365 # [s]  

  T_surface_K = 200  
  # using heat capacity C [J/m^2/K] for 100m deep water as example 
  C = 4.0e+08 
  albedo_earth = 0.3 # unitless  
  epsilon_earth = 1 # emissivity, unitless  
  epsilon_atmosphere = 0.77 # emissivity, unitless  

  include_greenhouse_effect = True  

  surface_temperatures = []  
  timesteps_years = []  

  def incoming_shortwave_radiation(alpha):  
      # dividing by 4 to map from circle to sphere  
      return SOLAR_RADIATION*(1-alpha)/4  

  def outgoing_longwave_radiation(temperature_K, epsilon):  
      # Boltzmann (1884)
      return epsilon * SIGMA * pow(temperature_K, 4)  

  # See model description paper section 1.2 for details  
  def compute_atmospheric_temperature(surface_temperature):  
      return surface_temperature/2**(1/4)  

  def convert_kelvin_to_celsius(temp_K):  
      return temp_K - 273.15  

  for t in range(0, 100):  

      radiative_imbalance_surface = incoming_shortwave_radiation(albedo_earth)
                              - outgoing_longwave_radiation(T_surface_K, epsilon_earth)  
	
      if include_greenhouse_effect:  
          reflected_longwave_radiation = outgoing_longwave_radiation(
            compute_atmospheric_temperature(T_surface_K), epsilon_atmosphere)
          radiative_imbalance_surface += reflected_longwave_radiation  
	
      T_surface_K += SECONDS_PER_YEAR * radiative_imbalance_surface / C  
	
      timesteps_years.append(t)  
      surface_temperatures.append(convert_kelvin_to_celsius(T_surface_K))  
{% endhighlight %}
<div class="caption">
	This is the same model as in the code snippet above. However, upon first look it is easily understandable what is happening in the model. Note that I decided to not extract `273.15` into a constant, simply because the function name already makes it clear what it happening. This code example was created building on the work of multiple online resources (Boergel, 2024; Mann & Gaudet, 2024; Rose & Scott-Brown, 2024).
</div>


# Conclusion

I hope this post, and especially the final example, could show you that it is quite simple to make code easily understandable. The little effort it takes will definitely be worth it, because it will save a lot of time when you or someone else has to revisit your code.

I believe that this still remaind valid in times of chatGPT and other code generation tools. Having the code well-readable and broken down into well-defined functions will help you ensure that the code is actually logically correct, and easily maintainable.



# References

- Boergel, F. (2024). Climate of the ocean. [https://florianboergel.github.io/climateoftheocean](https://florianboergel.github.io/climateoftheocean)
- Mann, M., & Gaudet, B. (2024). Meteo 469: From Meteorology to Mitigation: Understanding Global Warming. [https://www.e-education.psu.edu/meteo469/](https://www.e-education.psu.edu/meteo469/)
- McBain, M. (2024). Before I Sleep: Patterns and anti-patterns of data analysis reuse. [https://milesmcbain.com/posts/data-analysis-reuse/](https://milesmcbain.com/posts/data-analysis-reuse/)
- Rose, B. E. J., & Scott-Brown, J. (2024). The Climate Laboratory. [https://doi.org/10.5281/zenodo.10552644](https://doi.org/10.5281/zenodo.10552644)


