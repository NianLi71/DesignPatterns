# Design Patterns Summary
Most summary words from
* GoF
* https://refactoring.guru/design-patterns


## Abstract Factory
* Abstract Factory is a creational design pattern that lets you produce **families** of related objects without specifying their concrete classes.
* Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
* Think about UI components families


## Adapter
* Adapter is a structural design pattern that allows objects with **incompatible interfaces** to collaborate.
* A wrapper
* Two kind of adapters:
  * Object adapter, with object composition
  * Class adapter, with inheritance


## Composite
* Composite is a structural design pattern that lets you compose objects into **tree structures** and then work with these structures as if they were individual objects.
* Compose objects into **tree structures** to represent **part-whole** hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly .


## Strategy
* Strategy is a behavioral design pattern that lets you define a **family of algorithms**, put each of them into a separate class, and make their objects **interchangeable**.
* Define a **family of algorithms**, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.


## State
* State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.
* Allow an object to **alter its behavior** when its **internal state changes**. The object will appear to change its class.
* The State pattern is closely related to the concept of a Finite-State Machine
* The State pattern suggests that you create **new classes for all possible states** of an object and extract all **state-specific behaviors into these classes**.


## Observer
* Also known as: Event-Subscriber, Listener, Dependents, **Publish-Subscribe**
* Observer is a behavioral design pattern that lets you define a **subscription** mechanism to **notify multiple objects about any events** that happen to the object they’re observing.
* Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
* The object that has some interesting state is often called **subject**, but since it’s also going to notify other objects about the changes to its state, we’ll call it **publisher**. All other objects that want to track changes to the publisher’s state are called **subscribers**.


## Singleton
* Singleton is a creational design pattern that lets you ensure that **a class has only one instance**, while providing a **global access point** to this instance.


# 我的理解
* 我理解的Design Pattern就是和OO Design一起, 识别容易变化的地方, 并封装起来, 同时对扩展开放对修改封闭
* 像是构建一个尽可能抽象的主体framework, 在framework的一些hook点上做扩展, 但是对framework本身的修改应该尽可能避免


# 学习笔记
* https://refactoring.guru/design-patterns/ 适合经常翻看, 快速复习
* 对GoF, 每一个模式看前面的文字介绍就可以, 不需要看code, 再看看第一章, 就可以了
* HeadFirst design 确实不错可以多看几遍
 

# Links
A great design patterns learning website, you should love it: [The Catalog of Design Patterns](https://refactoring.guru/design-patterns/catalog)