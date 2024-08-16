import gradio as gr
from semantic_router import Route
from semantic_router.encoders import HuggingFaceEncoder
from semantic_router.layer import RouteLayer


# Define your routes
Dessert = Route(
    name="Dessert",
    utterances=[
        "Bourbon Chocolate Ice Cream. It fluffs up beautifully, doesn't melt rapidly during serving and it is one of the best chocolate flavours I have ever had. You know where the recipe is, go and get it.",
        "Chocolate pecan whiskey? Yes please and I dont even LIKE #whiskey This is the perfect blend of whiskey with a smooth butter pecan. Im best friends with the bottle now!",
        "You Put Your Chocolate in my Peanut Butter - skrewball peanut butter whiskey, accompani coffee liqueur, organic cocoa, house spiced coconut & almond cream, vegan roasted marshmallow with mexican chocolate cookie.",
        "What makes chocolate better??? â¬‡ï¸ â¬‡ï¸ â¬‡ï¸ Peanut Butter - Whiskey that is from olesmoky of course. Talk about elevating your next dish for an adult only event. This Peanut Butter Whiskey infused brownie batter dip is decadent and smooth. Recipe: 6oz cream cheese 3 tablespoons melted butter - in a large bowl beat these two ingredients together until smooth. ... In a separate bowl microwave 1 18oz package of brownie mix- I like the Ghirardelli mix - for 15 seconds at a time, stop and mix for a total of 1.5 minutes to heat treat the flour so it is safe to consume. When done combine with the other mixed ingredients. Mix in 2 tablespoons milk and 2 ounces olesmoky Peanut Butter Whiskey. I mixed in about 15 mini Reeseâ€™s peanut butter cups and sprinkles a little on top for presentation and served it with chocolate filled Biscoff cookies and pretzels. I hope you all enjoy this as much as we did, but please remember to be responsible. *This content and recipe contains alcohol and is for followers of the legal drinking age 21+ only. Iâ€™d like to thank olesmoky for another absolutely amazing opportunity to collaborate. The possibility are endless and so delicious. apexdropofficial #elevateyourlifestyle #olesmokytennesseemoonshine #olesmokywhiskey #olesmoky #whiskey #moonshine #cocktails #distilleries #chocolate #browine #foodie #snack #eat #peanutbutterlover #reeses #homecook #cooking #foodstagram #foodphotography #foodpics #foodlover #enjoy #drinkresponsibly #recipe #recipedeveloper",
        "Beautiful Lady.... Now the question is, what did you put in it? I prefer Chocolate Whiskey myself....lol",
        "sucker for a good pie and jackallenskitchen makes some great ones. They make a Chocolate Bourbon Pecan Pie which is one of my favorite desserts of all time as well as a Blondie Brownie Pie which is their take on the classic Tollhouse Cookie Pie which is delicious. ?? ??ï¸ #pie #pecanpie #cookie #austin #texas"
    ],
)



Nuts = Route(
    name="Nuts",
    utterances=[
        "I started cracking open pecans today for the Thanksgiving Pecan Pie! This is a favorite of mine that I serve with bourbon whipped cream! I also use these in my â€œHipsterâ€ Old Fashioned. (Pecan infused bourbon is so delicious!)",
        "For derby day, I served Old Fashioned Cocktail Pecans. These are a salty, sweet treat with a bit of heat and bourbon.",
        "Our Kentucky Maple Pecan is perfect for all the bourbon lovers out there! It has a delicious maple flavor with chopped pecans mixed in!",
        "Pecan Crusted Maple Bourbon Pumpkin w/Bourbon Cream Sauce. #yumyumyum #foodporn #pecan #makersmark #bourbon #tasty #damnimgood",
        "I looooove pecan pie. I found a delicious recipe for bourbon pecan pie with homemade bourbon whip cream. I may need to make one soon",
        "I've got the brownie mix and the bourbon walnuts soaking bring the cbd oil @chelseafree5",
    ]

)



Smoke = Route(
    name="Smoke",
    utterances=[
        "Ordered this amazing drink called campfire Coffee which features Cleveland Whiskey Magic Rabbit",
        "Ordered a pink drink & smoked old fashioned & both were delicious & had nice presentations",
        "Spare Ribs and Baby Backs. Used lard as binder and a mix of some rubs and brown sugar. Smoked at 250 for 3 hrs, sprayed with apple cider vinegar/bourbon/apple juice, double wrapped (paper and foil) with another spray and some spray butter for 2 hours, then since it wasnâ€™t ame time, I wrapped in a beach towel for about 1.5 hrs. They were so juicy and tender. Fell off the bone.",
        "Figured pecans and bourbon both like a little smoke so decided to smoke my Bourbon Pecan pie recipe for tomorrow. Lick test on the thermometer probe says its delicious. Will find out for sure tomorrow.",
        "Who loves a smoked cocktail? Iâ€™m making these white oak whiskey smokers for my upcoming show this fall, so of course I had to do some â€œproduct researchâ€ Works like a charm! Thanks to srodgers6 for the video assist #whiteoakwhiskeysmoker #whiskeysmoker #whiskey #bourbon #whiskeyglasses #cbrwoodcraft",
        "Oak Smoked Pork with Maple Bourbon Glaze. I smoked this over the Christmas period on a charcoal bed with whiskey oak barrel wood chips. The homemade rub was a mix of spices and salts, and the glaze was made from real maple syrup and buffalotrace. This was a fairly quick smoke only taking a couple of hours. #smoked #smokedmeat #smokedpork #bbqsmoker #smokedbbq #bourbon #maplesyrup #bbq #bbqporn #bbqfood",
    ],
)



Spices = Route(
    name="Spices",
    utterances=[
        "It's not for everyone, but almost everywhere sells Moscow mules. Ginger ale is also good. If there were Ginger wines, Ginger stouts, and Ginger Whiskeys, I'd probably drink those too.",
        "@vurnt22 Ginger beer and bourbon is one of two times I actually drink anything ginger-y. The other is ginger ale on an airplane because it just seems like you're supposed to.",
        "Curious to see how cinnamon forward it is. I love cinnamon flavor in bourbon, as long as it isn't too fiery.",
        "Bourbon Bacon Cinnamon Rolls ???? These Bourbon Bacon Cinnamon Rolls are a symphony of flavors and textures. Sweet and salty plus soft and crunchy plus a creamy glaze make decadent deliciousness! Read my review, find cooking tips, and get the recipe at https://www.hungrypinner.com/bourbon-bacon-cinnamon-rolls or link in bio. #cinnamonrolls #bourbon #bacon #breakfast #brunch #gastronomcocktails",
        "It doesnâ€™t help use your Calvados but I make apple cinnamon bourbon every winter. Just put apple slices and cinnamon sticks into a jar, fill with bourbon and let it sit 14 days, it makes the most wicked old fashioned.",
        "Tried this single malt from yellowstonebourbon and pleasantly surprised! I need to make a visit sometime ?? â€¢ This whiskey is fairly complex and gives me honey, cinnamon, oak vibes. â€¢ What cocktail ideas do we have?",

    ],
)


Fruits = Route(
    name="Fruits",
    utterances=[
        "I made a big batch of #Pineapple #WhiskeySours for tonight, and of course, I needed a tester drink.",
        "This apple cider whiskey cocktail is a delicious apple cider based alcohol drink that has Prosecco and whiskey inside. It is seasoned with cinnamon, apple slices and orange slices and makes for a wonderful Fall or Winter cocktail. I have been drinking this spiked apple cider cocktail for years now. I make it every Thanksgiving and Christmas and it is always a huge hit. For other fun cocktail ideas, try my Pumpkin Spice White Russian with Almond Milk, Healthy Homemade Strawberry Daiquiris. (moreâ€¦)The post Apple Cider Whiskey Cocktail appeared first on Perchance to Cook.",
        "Still do more research, but it looks like a tart cherry. Great for pies, and jams as the natural tartness balances well with the high sugar addition. If you are an enjoyer of alcohol, especially whiskey, they are great for making boozy cherries (Iâ€™ve only used whiskey, but other boozes work too, just gotta match flavors). This basically just means u put them in a jar for a couple weeks with a little sugar and they soak up the booze while flavoring is in return. They are really good additions to mixed drinks, and you can also eat them straight up (u will need to add more sugar if you want to do this tho, otherwise the combined aromatics will punch you in the sinuses)",
        "I was literally just thinking about making these!! Though, after reading another post about bourbon soaked chocolate covered cherries, the thought did cross my mind to do both for one batch. This could prove to be both a delicious and deadly combo",
        "Peach Hibiscus Bourbon Smash ?????? One of the best things about summer is fresh peaches â€” the juicier the better. And bourbon + peach is a match made in cocktail heaven. This is a drink Iâ€™ll be enjoying again and again this summer. Bottoms up! Ingredients: â€¢ 2 oz bourbon â€¢ 1/2 large peach,",
        "Ole Smoky Mango Habanero flavored Whiskey x Pineapple Juice",

    ],
)



# Encoder and route layer
encoder = HuggingFaceEncoder()
routes = [Dessert, Nuts, Smoke, Spices, Fruits]
r1 = RouteLayer(encoder=encoder, routes=routes)

# Function to process input
def classify_text(text):
    return r1(text)

# Gradio interface
iface = gr.Interface(
    fn=classify_text, 
    inputs=gr.Textbox(lines=2, placeholder="Enter a sentence here..."), 
    outputs="text",
    title="Semantic Router",
    description="Classify text based on pre-defined routes using semantic router."
)

if __name__ == "__main__":
    iface.launch()
