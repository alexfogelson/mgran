# mgran
So I should be doing homework, but I've kinda wanted to see how easy it is to make an n-gram model.

## Who to model?

Trump's been done a thousand times, anything serious isn't worth doing for this project. So I picked the most mimicable, most memeable robot I could create. The one true arbiter of facts and logic, of course. Ben Shapiro. 

### Data
A site called Podgist does really great work in transcribing podcasts. Worth checking out. I grabbed some of the free transcripts from them, although I haven't included them in this repo. Just a sample of what they outputed :)

### Technique

This uses multiple n-gram models. It will attempt to find a match with the largest number given, but models are also trained for lower n, just in case we've dug ourselves into a hole with the initial seed.
Also, there is some padding wiggle room, where the model thinks it has found nothing depsite an answer being derivable from history. This is intentional (and alterable), so that we don't simply use the highest n model at all times.

##### This isn't a political statement. You can love or hate the man. But you cannot deny that his cadence is hilarious and (respectfully) quite mockable.
