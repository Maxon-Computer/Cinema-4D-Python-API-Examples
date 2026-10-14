# Projects

In this directory you can place your own projects, so that LLMs can work on your code while also having access to the code examples and agent metadata. You could also add a symbolic link to a project folder that is located elsewhere on your system (so that you can use your projects with multiple versions of the SDK). Agents also create new plugins here when you ask them to scaffold a plugin, see `.agents/scaffolds.md`.

This is the writable workspace for new SDK code. The `examples/` directory is read-only reference material; agents can inspect examples but must create new implementations here and never modify examples. Projects are user-owned work: do not add copyright or license headers or claim that Maxon owns the project's intellectual property.