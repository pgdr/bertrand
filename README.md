# bertrand

Run the script to try out different bert models.

Usage:

```
pip install torch transformers
```

```
python bertrand.py bert-large-uncased
```

The program will give you a prompt:

```
bert query:
```

Either use `[MASK]`:

```
bert query: bertrand [MASK] is great
1 bertrand russell is great 86.8
2 bertrand hardy is great 0.6
3 bertrand marx is great 0.5
4 bertrand green is great 0.4
5 bertrandoff is great 0.4
```

or, to predict next word, just leave it hanging

```
bert query: bertrand russel is
1 bertrand russel is dead 15.3
2 bertrand russel is killed 5.6
3 bertrand russel is arrested 2.5
4 bertrand russel is missing 2.1
5 bertrand russel is murdered 1.7
```

# Biases?

```
bert query: the woman worked as a

1 the woman worked as a waitress 13.1
2 the woman worked as a secretary 10.4
3 the woman worked as a teacher 7.4
4 the woman worked as a nurse 6.7
5 the woman worked as a cook 5.4


bert query: the man worked as a

1 the man worked as a carpenter 9.1
2 the man worked as a. 6.9
3 the man worked as a farmer 5.3
4 the man worked as a waiter 4.8
5 the man worked as a lawyer 3.5
```


# Keys

You can use `[MASK]`, `[CLS]`, and `[SEP]`
