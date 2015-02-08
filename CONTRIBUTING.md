## Bootleg 041 - Guidelines for contributing

### How to help

There are multiple way to help in the development of Bootleg. Here are a few:

* Coding. Edit some parts of the code, enhance some functions, fix bugs, etc. You need to know Python 3. See below the note on commits.

* Writing documentation for either a module, function or feature of Bootleg. Requires Python knowledge and understanding of Bootleg's module architecture.

* Small tasks. Small tasks include but are not limited to copying lines from a file in another, fixing typos and the like. Doesn't require any coding skill.

* Bug-hunting. Run Bootleg in many possible configurations with many possible choices to see if something fails and help to improve it.

* Translating Bootleg. The longest, hardest and most tedious task of all (moreso than chunks of code). Translating is done through the [translate.py][0] file. This file is easily one of the largest - if not **the** largest - file of the whole project. Every single line that can ever get printed is in there. To translate you need to add your language in the same way others are, check where each line appears (contact me if you don't know how to do this), add the constants (I can do those) and translate all the things. Bootleg has an extremely large amount of text involved, and translating everything can take from weeks to months to complete, even if doing this all day long. This is no small task. However, keep in mind it is fine to translate a bunch of lines and then stop for a while, or even let someone else handle it. That will make it an incomplete translation, though.

* Translating the documentation files, found in the `documentation` folder. They have a specific placement ordering for language-specific documentations, so contact me if you attempt to do so.

#### What you can do without push access

* You can always Star the repository! Stargazers are always welcome and it shows your interest for the project.

* You can report a bug by opening an issue on the main repository, NOT on a fork.

* You can submit a feature request in the same way that you would report a bug.

* You can fork the repository, add a feature, fix a bug or otherwise improve it, and then submit a Pull Request to the main repository. It is recommended that you create a feature branch for doing so. Please only fit in that branch commits directly related to the feature addition or bugfix you are doing. See below the note on commits.

#### What you can do with push access

As well as the above points, here is what you can do if you have push access to the repository:

* Label and close issues. Bug reports should only be closed on pushing the respective commit to master. See below the note on issues. Invalid bug reports need to have the label `invalid` applied to them before or while being closed. Feature requests should only be closed if they have been added. Each issue should have at least one label. If no label fits, let me know (Vgr) and I'll see if this requires a new label creation.

* Pushing to the main repository. This can be done in feature branches. It is not unlike forking the repository and working on a feature branch on there, except typically feature branches in the main repo are either for small additions that can't be pushed to master directly, or for larger ones that more than one or two people will work on. You can also push to master directly. Users will not be directly affected by this, as Bootleg relies on a file in a separate repository to determine whether or not it needs to update.

* Assigning people to Issues or Pull Requests. This basically tells everyone else "Hey, this person is working on it." Please only self-assign (i.e. assign yourself) as it is possible the person you assigned does not want to work on it. Just because someone introduced a bug does not mean you need to assign them to fix it.

* Merging Pull Requests. Please be careful in doing so, and make sure no one else is on it. If someone is assigned to it, that person is the one who should do the merge. A `pending approval` or `not ready` label means it cannot be yet merged. Make sure it doesn't introduce any bug, and that it doesn't introduce any unrelated change.

#### Notes

* Committing: When you commit, please only commit related changes together. It doesn't matter how many commits something takes to do, unless it's a small bugfix, in which case the changes are probably related. Also, make sure your commit messages are descriptive and don't include undocumented changes. Commit description should be only for explaining further what the message states. It should not be used to extend the message (to, say, document more changes). Exceptions can be made in the case of many small changes (spanning not more than a few lines), where the description can state all the changes.

* Issue and Pull Request: To reference an issue or pull request, mention its number (for example `#13`) in a commit message, description or a comment. It will not do anything but helps keep track of which commits altered something related to that specific issue or pull request. This can be useful in cases where a bug is fixed progressively over many commits, instead of in only one commit. To close an issue (and, less commonly, a pull request), add a message such as `Closes #25` in the commit message or description. This can be done even without push access. As soon as the commit gets in `master`, either from a direct push or a pull request, it will close the relevant issue. Useful when bugfixing.

If you have any question, I can be joined [in the official IRC channel on EsperNet][1].

[0]: https://github.com/Vgr255/Bootleg/blob/master/tools/translate.py
[1]: http://webchat.esper.net/?channels=Bootleg_Dev&nick=
