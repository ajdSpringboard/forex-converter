### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

```The syntax is quite different, python is dynamically-typed whereas javascript is loosely-typed, javascript can run in a web browser, and there a much different libraries and frameworks available for each language.```

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  ```By using the get() method or try/except blocks```

- What is a unit test?

```A unit test focuses mainly on just a specific part of code and makes sure that part does its job correctly.```

- What is an integration test?

```An integration test tests how different components in a system work together and ensures everything interacts appropriately.```

- What is the role of web application framework, like Flask?

```The role of a web app framework is to provide a set of libraries and tools to build web applications more easily and efficiently, and provides support for things like: routing, testing, templates, security, etc```

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  ```A route url is better for important or less dynamic pages and a query parameter can be better for things like search results or other dynamic pages that don't deserve their own dedicated page```

- How do you collect data from a URL placeholder parameter using Flask?

```You put it as an variable in the function paranthesis of your route definition```

- How do you collect data from the query string using Flask?

```request.args.get('query_name')```

- How do you collect data from the body of the request using Flask?

```request.data or request.get_json()```

- What is a cookie and what kinds of things are they commonly used for?

```A cookie is a piece of data that is stored client-side and contains information based on that user's activity```

- What is the session object in Flask?

```It is similar to cookies, but utilizes a unique session ID and encrypts the data using the Flask app's secret key variable```

- What does Flask's `jsonify()` do?

```It converts a python object into JSON```
