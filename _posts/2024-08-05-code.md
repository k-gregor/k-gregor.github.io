---
layout: post
title: Proper variable naming
date: 2024-08-05 15:09:00
description: A trivial yet sometimes overlooked aspect of making your code readable
tags: code
categories: code
featured: true
---

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

In languages like Python you can even have named function parameters. We can thus extract the code into a well-named function (which we can then also easily test) and have a very understandable function call:

{% highlight python linenos %}
  def calculate_bank_account_value(initial_investment, interest_rate, time_in_years):
    return initial_investment*(1+interest_rate)**time_in_years
  
  calculate_bank_account_value(initial_investment=1, interest_rate=0.02, time_in_years=8)
{% endhighlight %}
