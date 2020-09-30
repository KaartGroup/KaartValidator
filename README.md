# KaartValidator
Kaart Validator


# Suggested Settings
## JOSM
In JOSM Preferences, go to "Advanced Preferences" and change "mirror.maxtime"
from "604800" (7 days)to "14400" (4 hours). This number is seconds between
update checks for _any_ mirror that you have in preferences. In my preferences
file, there were about 25 external files. Please _do not_ set it any lower than
4 hours (14400 seconds).

# DwarfTeamValidator
Validator for the Dwarf Team at Kaart Group, LLC.

## The Validator
The aim of this tool is to help individuals (particularly those on the Dwarf Team) make more consistent, and more accurate change-sets for the Brazil project. This tool was designed by Andrew Piechota and RD Clare with the help of Taylor Smock. Any improvements or requests are appreciated. Please send them to either our slack client or email us at [Andrew](mailto:andrew.piechota@kaartgroup.com), [RD](mailto:rd.clare@kaartgroup.com) or [Taylor](mailto:taylor.smock@kaartgroup.com). Thank you for using our validation tool!

## Contributing

1) Any _new_ tag-based check _MUST_ have `assertMatch` and `assertNoMatch` clauses.
2) Any _modified_ tag-based check _MUST_ have `assertMatch` and `assertNoMatch` clauses for the modifications.
3) Run `./make.py` _PRIOR TO_ commiting, and commit the result.
4) The `git` commit _MUST_ have your email address (_NOT_ the anonymous GitHub email address)
5) You _MUST_ test _ALL_ of the changed files in JOSM with `validator.check_assert_local_rules` set to `true`. If you see any failures, they _MUST_ be fixed. Failure to do so _WILL_ result in a response with the issue, but _WILL_ increase the amount of time before the merge request is merged.
6) The commit message must be _meaningful_. It must describe what you changed and why. An example of the problem being fixed _would not_ be remiss. See the section on "Patch formatting and changelogs" at https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/process/5.Posting.rst for more information.
7) Use the module functionality. To add a module to a specific project, modify the appropriate file under `project` such that the `modules` array contains the filename of the new module.
