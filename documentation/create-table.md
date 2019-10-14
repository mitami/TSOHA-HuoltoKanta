```
CREATE TABLE Action (
  id INTEGER NOT NULL,
  name VARCHAR(30),
  due DATE,
  desc VARCHAR(255),
  done BOOLEAN,
  FOREIGN KEY (target_id) REFERENCES Target,
  PRIMARY KEY (id)
);
```

```
CREATE TABLE Location (
  id INTEGER NOT NULL,
  name VARCHAR(30),
  PRIMARY KEY (id)
);
```

```
CREATE TABLE Target (
  id INTEGER NOT NULL,
  name VARCHAR(20),
  FOREIGN KEY (location_id) REFERENCES Location,
  PRIMARY KEY (id)
);
```

```
CREATE TABLE Executor (
  id INTEGER NOT NULL,
  name VARCHAR(30),
  title VARCHAR(30),
  PRIMARY KEY (id)
);
```

```
CREATE TABLE Executor_Action (
  FOREIGN KEY (action_id) REFERENCES Action,
  FOREIGN KEY (executor_id) REFERENCES Executor
);
```
