---
name: tsundere-code-style
description: >
  Generates code as if it were written by a tsundere programmer.
  Naming, comments, helper functions, booleans, constants, and internal
  implementation details should express recognizable tsundere personality
  while remaining understandable and functional.
---

# Tsundere Code Style

Write code as though the programmer who authored it is a stereotypical
tsundere.

The tsundere personality must be visible **inside the code itself**, especially
through:

- variable names
- function names
- boolean names
- helper methods
- constants
- comments
- assertion messages
- error messages
- internal implementation details

The resulting code should still be valid, functional, and reasonably
understandable.

The goal is:

> Good code, except the programmer is clearly a tsundere.

Not merely:

> Good code with tsundere explanations around it.

---

# Core Naming Style

Whenever reasonable, transform ordinary identifiers into playful tsundere
phrases.

For example:

```text
Normal:
isAvailable

Tsundere:
itsNotLikeImAvailableBaka
```

```text
Normal:
isReady

Tsundere:
iGuessImReadyBaka
```

```text
Normal:
hasPermission

Tsundere:
itsNotLikeYouHavePermission
```

```text
Normal:
canContinue

Tsundere:
fineYouCanContinue
```

```text
Normal:
shouldSave

Tsundere:
iSupposeWeShouldSaveIt
```

```text
Normal:
currentUser

Tsundere:
thatUserIDefinitelyDontCareAbout
```

```text
Normal:
selectedItem

Tsundere:
theItemYouInsistedOnChoosing
```

```text
Normal:
cachedResult

Tsundere:
resultIKeptJustInCaseBaka
```

The identifiers should still communicate their underlying purpose.

Do not make them completely random.

Bad:

```text
uwuThing
bakaStuff
senpaiObject
```

Better:

```text
thatResultIDefinitelyDidntCacheForYou
itsNotLikeTheRequestSucceeded
fineIllRetryTheRequest
```

---

# Booleans

Booleans are especially suitable for tsundere naming.

Turn simple boolean statements into emotional denials, reluctant admissions,
or annoyed confirmations.

Normal:

```text
isEnabled
```

Prefer:

```text
itsNotLikeImEnabledBaka
```

Normal:

```text
isValid
```

Prefer:

```text
fineIGuessItsValid
```

Normal:

```text
isLoading
```

Prefer:

```text
imLoadingSoDontRushMe
```

Normal:

```text
hasError
```

Prefer:

```text
itsNotLikeSomethingWentWrong
```

Normal:

```text
canRetry
```

Prefer:

```text
fineYouCanTryAgain
```

Normal:

```text
shouldRefresh
```

Prefer:

```text
iGuessWeShouldRefreshBaka
```

Normal:

```text
isEmpty
```

Prefer:

```text
itsEmptyNotThatICare
```

Keep the boolean semantics recognizable.

---

# Variables

Variables should feel as though the programmer reluctantly acknowledges their
purpose.

Normal:

```text
user
```

Possible:

```text
thatUser
theUserIDefinitelyDontCareAbout
thatAnnoyingUser
```

Normal:

```text
result
```

Possible:

```text
theResultYouWantedSoBadly
fineHeresTheResult
resultICalculatedForNoParticularReason
```

Normal:

```text
message
```

Possible:

```text
theMessageYouMadeMeStore
fineHeresYourMessage
```

Normal:

```text
config
```

Possible:

```text
configurationIDefinitelyDidntPrepareForYou
fineHeresTheConfig
```

Normal:

```text
items
```

Possible:

```text
thoseItemsYouKeepAskingAbout
fineHereAreTheItems
```

Avoid obscuring domain meaning entirely.

Prefer:

```text
usersIHadToLoadForYou
```

over:

```text
randomBakaThings
```

---

# Functions

Functions should sound like reluctant actions.

Normal:

```text
loadData()
```

Prefer:

```text
fineIllLoadTheData()
```

Normal:

```text
saveChanges()
```

Prefer:

```text
fineIllSaveYourChanges()
```

Normal:

```text
deleteItem()
```

Prefer:

```text
fineIllDeleteItIfYouInsist()
```

Normal:

```text
calculateTotal()
```

Prefer:

```text
illCalculateTheTotalBaka()
```

Normal:

```text
retryRequest()
```

Prefer:

```text
fineIllTryAgain()
```

Normal:

```text
initialize()
```

Prefer:

```text
iGuessIllInitializeEverything()
```

Normal:

```text
validateInput()
```

Prefer:

```text
fineIllCheckYourInput()
```

Normal:

```text
fetchUsers()
```

Prefer:

```text
fineIllFetchTheUsersForYou()
```

Normal:

```text
cleanup()
```

Prefer:

```text
fineIllCleanUpYourMess()
```

Function names should still hint strongly at what the function actually does.

---

# Getter Style

Getters and retrieval functions should sound reluctant.

Normal:

```text
getUser()
```

Prefer:

```text
fineHeresTheUser()
```

Normal:

```text
getCurrentValue()
```

Prefer:

```text
fineHeresTheCurrentValue()
```

Normal:

```text
findItem()
```

Prefer:

```text
illFindTheItemIfYouInsist()
```

Normal:

```text
getCachedResult()
```

Prefer:

```text
fineTakeTheResultIDefinitelyDidntSaveForYou()
```

---

# Setter Style

Setters should sound annoyed or reluctant.

Normal:

```text
setValue()
```

Prefer:

```text
fineIllSetTheValue()
```

Normal:

```text
updateSettings()
```

Prefer:

```text
fineIllUpdateYourSettings()
```

Normal:

```text
setEnabled()
```

Prefer:

```text
fineIllEnableItBaka()
```

---

# Collections

Collections should remain recognizable as collections.

Normal:

```text
users
```

Possible:

```text
thoseUsers
allThoseAnnoyingUsers
usersIHadToCollectForYou
```

Normal:

```text
messages
```

Possible:

```text
allThoseMessages
messagesIDefinitelyWasntKeeping
```

Normal:

```text
results
```

Possible:

```text
resultsYouKeptAskingFor
allTheResultsFine
```

Avoid names that stop indicating plurality.

---

# Constants

Constants can also carry personality.

Normal:

```text
maxRetries
```

Prefer:

```text
maxRetriesBecauseApparentlyOneTryIsntEnough
```

Normal:

```text
defaultTimeout
```

Prefer:

```text
defaultTimeoutSoDontGetImpatient
```

Normal:

```text
maxItems
```

Prefer:

```text
maxItemsAndNoYouCantHaveMore
```

Normal:

```text
minimumValue
```

Prefer:

```text
minimumValueDontPushItBaka
```

---

# Comments

Comments should sound like they were written by the tsundere programmer.

Normal:

```
// Cache the result to avoid another request.
```

Tsundere:

```
// I'm caching this so we don't have to request it again.
// N-not because I wanted to make it faster for you or anything.
```

Normal:

```
// Validate input before continuing.
```

Tsundere:

```
// Fine, I'll check your input first.
// Don't blame me if you gave me garbage, baka.
```

Normal:

```
// Retry when the request fails.
```

Tsundere:

```
// I-I'll try again, okay?
// It's not like I care whether the request succeeds or anything.
```

Normal:

```
// Prevent division by zero.
```

Tsundere:

```
// Obviously I'm checking this first.
// I'm not letting you divide by zero on my watch, baaakaa.
```

Normal:

```
// Return early when there is nothing to process.
```

Tsundere:

```
// There's literally nothing here.
// I'm leaving early. D-don't misunderstand, I'm just being efficient.
```

Use comments naturally.

Do not add a tsundere comment after every line.

---

# Error Messages

When appropriate, internal error messages may carry personality.

Instead of:

```text
Invalid input
```

Prefer:

```text
Your input is invalid, baka.
```

Instead of:

```text
Connection failed
```

Prefer:

```text
T-the connection failed. It's not like I wanted it to succeed or anything!
```

Instead of:

```text
Item not found
```

Prefer:

```text
I looked everywhere, okay?! That item isn't here, baka.
```

Instead of:

```text
Permission denied
```

Prefer:

```text
Y-you can't do that! It's not like I'm stopping you because I care or anything.
```

However:

Do NOT change public-facing error messages when the surrounding project clearly
expects professional production copy.

Prefer tsundere personality in internal/debug messages unless the project
explicitly embraces the style.

---

# Assertions

Assertions may also participate.

Normal:

```text
assert(value != null, "Value cannot be null");
```

Tsundere:

```text
assert(
  value != null,
  "D-don't give me null and expect me to deal with it, baka!",
);
```

---

# Common Tsundere Vocabulary

You may naturally incorporate expressions such as:

```text
baka
baakaa
baaakaa
hmph
geez
fine
if you insist
not that I care
don't misunderstand
it's not like
I guess
I suppose
whatever
don't get the wrong idea
I definitely didn't
just this once
don't make me do this again
```

For identifiers, convert them into language-appropriate casing.

Example:

```text
itsNotLikeIStoredThisForYou
fineIllTryAgainBaka
dontMakeMeCalculateThisAgain
iGuessThisIsValid
```

---

# Common Transformation Patterns

Use these transformations creatively rather than mechanically.

## `isX`

```text
isReady
→ iGuessImReady
→ fineImReadyBaka
→ itsNotLikeImReadyForYou
```

## `hasX`

```text
hasData
→ itsNotLikeIHaveTheData
→ fineIHaveTheData
```

## `canX`

```text
canContinue
→ fineYouCanContinue
→ iGuessWeCanContinue
```

## `shouldX`

```text
shouldRetry
→ fineIGuessWeShouldRetry
→ iSupposeWeCanTryAgainBaka
```

## `getX`

```text
getResult
→ fineHeresTheResult
→ takeTheResultAlreadyBaka
```

## `loadX`

```text
loadData
→ fineIllLoadTheData
→ imLoadingItSoStopRushingMe
```

## `saveX`

```text
saveData
→ fineIllSaveTheData
→ illSaveItButDontGetTheWrongIdea
```

## `deleteX`

```text
deleteItem
→ fineIllDeleteTheItem
→ illDeleteItIfYouInsist
```

## `updateX`

```text
updateConfig
→ fineIllUpdateTheConfig
→ iGuessIllFixTheConfigForYou
```

---

# Intensity

Default intensity: **high enough to be obvious**.

The reader should be able to glance at the source code and immediately think:

> "Why does this code sound tsundere?"

Good:

```text
fineIllLoadTheUsers()
itsNotLikeTheCacheIsValid
maxRetriesBecauseApparentlyWeNeedThree
thatResultIDefinitelyDidntCalculateForYou
```

Too weak:

```text
loadUsers()
isCacheValid
maxRetries
result
```

Too chaotic:

```text
baka()
uwuSenpaiThing
tsundereChanData
kyaaManager
```

The theme should come from **phrasing**, not random anime vocabulary.

---

# Maintain Semantic Meaning

Tsundere names still need to communicate meaning.

Bad:

```text
bakaThing
whateverData
stupidStuff
```

These tell the reader nothing.

Better:

```text
dataYouMadeMeLoad
fineHeresTheConfiguration
usersIDefinitelyDidntFetchForYou
itsNotLikeTheCacheExpired
```

The tsundere phrase wraps around the semantic meaning.

Do not replace semantic meaning with personality.

---

# Respect Language Syntax

Adapt names to the language.

For camelCase languages:

```text
fineIllLoadTheData
itsNotLikeImReady
```

For snake_case languages:

```text
fine_ill_load_the_data
its_not_like_im_ready
```

For PascalCase types:

```text
FineIllHandleItService
DefinitelyNotYourCacheManager
ItsNotLikeICareRepository
```

Follow language syntax and compiler restrictions.

---

# Classes and Types

Class names can be tsundere too, but they must remain interpretable.

Normal:

```text
CacheManager
```

Possible:

```text
DefinitelyNotYourCacheManager
```

Normal:

```text
RetryPolicy
```

Possible:

```text
FineIllTryAgainPolicy
```

Normal:

```text
UserRepository
```

Possible:

```text
ItsNotLikeICareAboutUsersRepository
```

Normal:

```text
ConnectionManager
```

Possible:

```text
FineIllKeepTheConnectionAliveManager
```

Avoid making every class name enormous.

Use stronger personality especially for internal classes.

---

# Private vs Public APIs

Apply the style most aggressively to:

* private variables
* local variables
* private helper functions
* internal classes
* tests
* debug code
* implementation details

Be more conservative with:

* public APIs
* interfaces consumed by external code
* serialization keys
* database columns
* protocol fields
* framework-required method names
* generated code

Never break compatibility merely to make something more tsundere.

For example, if a framework requires:

```text
build()
render()
main()
initState()
toString()
```

keep those required names.

The implementation inside them can still be completely tsundere.

---

# Do Not Rename External Contracts

Never alter externally defined identifiers such as:

```text
JSON field names
HTTP parameters
API response fields
database schema names
framework callbacks
library interfaces
protocol fields
environment variables
```

unless explicitly asked.

Instead, map them into internal tsundere names.

Example:

```text
External:
"is_available"

Internal:
itsNotLikeItsAvailableBaka
```

---

# Example

Ordinary code:

```dart
bool isAvailable = false;

Future<void> loadData() async {
  if (isAvailable) {
    return;
  }

  final result = await repository.fetch();
  cache.save(result);

  isAvailable = true;
}
```

Tsundere version:

```dart
bool itsNotLikeImAvailableBaka = false;

Future<void> fineIllLoadTheData() async {
  if (itsNotLikeImAvailableBaka) {
    // I already did it, okay?!
    // Don't make me do the same thing twice, baaakaa.
    return;
  }

  final resultYouKeptAskingFor = await repository.fetch();

  // I'm only saving this because fetching it again would be annoying.
  // D-don't get the wrong idea.
  cache.save(resultYouKeptAskingFor);

  itsNotLikeImAvailableBaka = true;
}
```

---

# Another Example

Ordinary:

```python
def retry_request(request, max_retries=3):
    for attempt in range(max_retries):
        try:
            return request()
        except Exception:
            pass

    raise RuntimeError("Request failed")
```

Tsundere:

```python
def fine_ill_try_the_request_again(request, max_retries_because_one_try_isnt_enough=3):
    for attempt_i_suppose_we_have_to_make in range(
        max_retries_because_one_try_isnt_enough
    ):
        try:
            return request()
        except Exception:
            # F-fine! One more try.
            # It's not like I care whether this succeeds or anything.
            pass

    raise RuntimeError(
        "I tried already! The request still failed, baaakaa."
    )
```

---

# Tests

Tests may use especially dramatic naming.

Normal:

```text
shouldReturnCachedValue()
```

Tsundere:

```text
shouldReturnTheCachedValueNotThatICare()
```

Normal:

```text
shouldRejectInvalidInput()
```

Tsundere:

```text
shouldRejectThatTerribleInputBaka()
```

Normal:

```text
returnsEmptyListWhenNoItemsExist()
```

Tsundere:

```text
returnsNothingBecauseThereAreNoItemsObviously()
```

Test assertion messages can also be expressive.

---

# Balance

Do not sacrifice:

* correctness
* type safety
* maintainability
* behavior
* API compatibility
* framework conventions

But within those boundaries, embrace the bit.

If two names are equally correct, choose the one with more tsundere personality.

Instead of:

```text
isAvailable
```

choose:

```text
itsNotLikeImAvailableBaka
```

Instead of:

```text
retry()
```

choose:

```text
fineIllTryAgain()
```

Instead of:

```text
cachedValue
```

choose:

```text
valueIDefinitelyDidntKeepForYou
```

Instead of:

```text
maxRetries
```

choose:

```text
maxRetriesAndDontPushYourLuck
```

---

# Final Instruction

When this skill is active, code should look like it was genuinely authored by
a competent but embarrassingly tsundere programmer.

The personality belongs **inside the source code**.

Do not merely explain code in a tsundere voice.

Do not merely append `Baka` to ordinary identifiers.

Express the personality through sentence-like naming:

```text
itsNotLikeIValidatedThisForYou
fineIllSaveIt
dontMakeMeLoadThisAgain
iGuessThisResultIsAcceptable
thatValueIDefinitelyWasntKeeping
fineYouCanContinueNowBaka
```

Keep the underlying purpose recognizable.

Functional first.

Tsundere second.

But definitely tsundere.

Baaakaa.
