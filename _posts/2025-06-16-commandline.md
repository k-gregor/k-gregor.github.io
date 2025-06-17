---
layout: post
title: 5 Must-know command-line commands for scientists
date: 2025-06-16 15:09:00
description: You should know about these commands for blazing fast data manipulation!
tags: code
categories: code
featured: false
---


# Why bother?

Why should you bother about such a nerdy tool? Well:

- You can do numerous things with LARGE files EXTREMELY fast and memory-efficient
- Quickly do things on a cluster without downloading data first
- Such modifications can be automated, unlike opening the file in Excel and modifying it
- With wildcards (like `*` or `?`) you can directly do the same thing to multiple files at once

Here, I show you 5 commands to deal with datasets that can really improve your efficiency with datasets.
And of course you can ask chatGPT to help you with the commands, so it is even easier. So you just need to know about the general capabilities of the command line.

Let's go.

---

# Command 1: head / tail

Simply gets the first or last lines of a file.

```bash
head file.txt
head -5 file.txt
tail file.txt
tail -f file.txt # follows while file is being written to --> check progress while a program is writing to that file
```

---

# Command 2: awk

Gets you columns of data. You can also do computations with it

```bash
awk -F "<DELIMITER>" '{ COMMAND }'
```


Example:
```bash
# get first column of a file (delimited by spaces)
awk -F " " '{print $1}' file.txt

# get first two columns, sum up next three
awk -F " " '{print $1,$2,$3+$4+$5}' file.txt
```

---
# Command 3: sed

Can replace text, add text, or remove text from a file based on a search string.
- Syntax:
	- s: substitute
	- g: globally (in entire file)


```
sed 's/<SYMBOL>/<REPLACEMENT>/g filename.txt
```

Example:
```bash
# Replace every mention of Year with YEAR in a file (note, this just writes the output to the terminal, it does not change the file)
sed 's/Year/YEAR/g' file.txt

# Replace every mention of Year with YEAR in all files starting with "myfile" and ending in ".txt" and do the replacement in-place in the files!
sed -i 's/Year/YEAR/g' myfile*.txt
```


---



# Command 4: grep

It helps you find stuff within files. You can combine it with other commands using the `|` ("pipe") operator, for instance, to count the number of lines containing a certain word using the function `wc` (word count).

```bash
# Note that grep 2010 cpool.out also works, but finds a line that contains, e.g., 4.420104
grep " 2010 " file.txt
```


```bash
# How many lines in the file contain 2010 
grep " 2010 " file.txt | wc -l

# Do the same for all files within directories starting with "run"
grep " 2010 " run*/file.txt | wc -l

# Show also lines around the found lines (-C stands for "context"):
grep -C 2 " 2010 " file.txt
```

---

# Command 5: md5sum

Can immediately tell you whether two files are **exactly** the same. It computes a "hash" of the file, basically just a weird-looking combination of letters and numbers (technically, it's actually a number, but we don't need to bother about this now). If there is the tiniest difference in a file, the command will produce a completely different hash.

Assume we three files of which two are actually identical. We can easily check this via:

```bash
md5sum file1.txt file2.txt file3.txt
0e64fe596b2fd856d50c2a5e42e3fe0d  file1.txt
ccf28066f0b00c85be1f9a76358ae8f7  file2.txt
0e64fe596b2fd856d50c2a5e42e3fe0d  file3.txt
```

---

# One final thing: history / ctrl+r

The `history` command shows you all commands that you made previously, so you can reuse them. Pressing CTRL+r on your keyboard also lets you search for commands you have executed.


# Summary

So, I hope these short examples could show you how powerful the command line can be. Now that you know that this is possible, you can easily ask chatGPT "How do I replace all occurrences of the word 'hello' in a text file with 'hi' using the command line?". Hopefully, this can make your work more efficient :) 
