# 27 Philosophers by centrality 

philosophers_data = {
        "Aristotle": {
            "Era": "BC",
            "Year": 322,
            "Attributes": ["Aristotelianism", "Ancient_Greek_philosophy", "Natural_philosophy"],
            "Influences": ["Plato", "Socrates", "Heraclitus"]
        },
        "Plato": {
            "Era": "BC",
            "Year": 348,
            "Attributes": ["Platonism", "Ancient_Greek_philosophy", "Political_philosophy"],
        "Influences": ["Socrates", "Heraclitus"]
        },
        "Immanuel_Kant": {
            "Era": "AD",
            "Year": 1804,
            "Attributes": [
                "Kantianism",
                "Classical_liberalism",
                "Empirical_realism",
                "liberal_naturalism",
                "Transcendental_idealism",
                "German_idealism",
                "Age_of_Enlightenment",
                "German"
            ],
            "Influences": ["Aristotle", "Plato", "Jean-Jacques_Rousseau", "René_Descartes", "Adam_Smith"]
        },
        "Georg_Wilhelm_Friedrich_Hegel": {
            "Era": "AD",
            "Year": 1831,
            "Attributes": ["Hegelianism", "Absolute_idealism", "German_idealism", "19th-century_philosophy", "German"],
            "Influences": ["Aristotle", "Immanuel_Kant", "Plato", "Jean-Jacques_Rousseau", "Baruch_Spinoza", "Johann_Gottlieb_Fichte", "Adam_Smith"]
        },
        "Karl_Marx": {
            "Era": "AD",
            "Year": 1883,
            "Attributes": ["Marxism", "Communism", "19th-century_philosophy", "German"],
            "Influences": ["Immanuel_Kant", "Georg_Wilhelm_Friedrich_Hegel", "Jean-Jacques_Rousseau", "Adam_Smith"]
        },
        "Friedrich_Nietzsche": {
            "Era": "AD",
            "Year": 1900,
            "Attributes": ["Nietzscheanism", "Existentialism", "19th-century_philosophy", "German"],
            "Influences": ["Baruch_Spinoza", "Heraclitus", "Arthur_Schopenhauer"]
        },
        "Augustine_of_Hippo": {
            "Era": "AD",
            "Year": 430,
            "Attributes": ["Augustinianism", "Christianity", "Neoplatonism"],
            "Influences": ["Aristotle", "Plato", "Socrates", "Plotinus", "Cicero"]
        },
        "Thomas_Aquinas": {
            "Era": "AD",
            "Year": 1274,
            "Attributes": ["Christianity", "Scholasticism", "Thomism"],
            "Influences": ["Plato", "Aristotle", "Socrates", "Augustine_of_Hippo", "Cicero"]
        },
        "Jean-Jacques_Rousseau": {
            "Era": "AD",
            "Year": 1778,
            "Attributes": ["Rousseauism", "Social_contract", "Age_of_Enlightenment", "Political_philosophy", "French"],
            "Influences": ["Plato", "Socrates", "Baruch_Spinoza", "John_Locke", "Thomas_Hobbes", "Voltaire"]
        },
        "David_Hume": {
            "Era": "AD",
            "Year": 1776,
            "Attributes": ["Humeanism", "Empiricism"],
            "Influences": ["Jean-Jacques_Rousseau", "John_Locke", "Thomas_Hobbes", "Cicero", "Adam_Smith"]
        },
        "Baruch_Spinoza": {
            "Era": "AD",
            "Year": 1677,
            "Attributes": ["Spinozism", "Rationalism", "Pantheism", "Cartesianism"],
            "Influences": ["René_Descartes", "Thomas_Hobbes", "Niccolò_Machiavelli"]
        },
        "René_Descartes": {
            "Era": "AD",
            "Year": 1650,
            "Attributes": ["Cartesianism","Rationalism","Dualism","Age_of_Enlightenment","Augustinianism"],
            "Influences": ["Plato", "Aristotle", "Augustine_of_Hippo", "Thomas_Aquinas"]
        },
        "Socrates": {
            "Era": "BC",
            "Year": 399,
            "Attributes": ["Socraticism", "Ancient_Greek_philosophy"],
            "Influences": []
        },
        "John_Locke": {
            "Era": "AD",
            "Year": 1704,
            "Attributes": ["Lockean_liberalism", "Empiricism", "Social_contract", "Age_of_Enlightenment", "Political_philosophy"],
            "Influences": ["René_Descartes", "Baruch_Spinoza", "Thomas_Hobbes"]
        },
        "Gottfried_Wilhelm_Leibniz": {
            "Era": "AD",
            "Year": 1716,
            "Attributes": ["Leibnizianism", "Rationalism", "Monadology", "German"],
            "Influences": ["Plato", "Aristotle", "René_Descartes", "Baruch_Spinoza", "Thomas_Hobbes"]
        },
        "Sigmund_Freud": {
            "Era": "AD",
            "Year": 1939,
            "Attributes": ["Psychoanalysis", "Psychology", "German"],
            "Influences": ["Plato", "Friedrich_Nietzsche", "Søren_Kierkegaard"]
        },
        "Friedrich_Wilhelm_Joseph_Schelling": {
            "Era": "AD",
            "Year": 1854,
            "Attributes": ["German_idealism", "Transcendental_idealism", "Absolute_idealism", "19th-century_philosophy", "German"],
            "Influences": ["Immanuel_Kant", "Baruch_Spinoza", "Plato", "Aristotle", "Gottfried_Wilhelm_Leibniz", "Plotinus", "Johann_Gottlieb_Fichte"]
        },
        "Martin_Heidegger": {
            "Era": "AD",
            "Year": 1976,
            "Attributes": ["Existentialism", "Phenomenology", "Ontology", "German"],
            "Influences": ["Aristotle", "Augustine_of_Hippo", "Plato", "Friedrich_Nietzsche","Edmund_Husserl", "Søren_Kierkegaard", "Heraclitus"]
        },
        "Plotinus": {
            "Era": "AD",
            "Year": 270,
            "Attributes": ["Neoplatonism", "Mysticism"],
            "Influences": ["Plato", "Aristotle", "Heraclitus"]
        },
        "Edmund_Husserl": {
            "Era": "AD",
            "Year": 1938,
            "Attributes": ["Phenomenology", "Epistemology", "German", "Austria"],
            "Influences": ["René_Descartes", "David_Hume", "Immanuel_Kant", "Gottfried_Wilhelm_Leibniz", "Plato"]
        },
        "Ludwig_Wittgenstein": {
            "Era": "AD",
            "Year": 1938,
            "Attributes": ["Analytic_philosophy", "Logical_positivism", "Linguistic_philosophy", "Austra"],
            "Influences": ["Baruch_Spinoza", "Immanuel_Kant", "Friedrich_Nietzsche", "Sigmund_Freud", "Augustine_of_Hippo", "Søren_Kierkegaard", "Arthur_Schopenhauer"]
        },
        "Søren_Kierkegaard": {
            "Era": "AD",
            "Year": 1855,
            "Attributes": ["Existentialism", "Christian_existentialism", "Philosophy_of_religion"],
            "Influences": ["Augustine_of_Hippo", "René_Descartes", "Georg_Wilhelm_Friedrich_Hegel", "Immanuel_Kant", "Plato", "Friedrich_Wilhelm_Joseph_Schelling", "Socrates"]
        },
        "Johann_Gottlieb_Fichte": {
            "Era": "AD",
            "Year": 1814,
            "Attributes": ["German_idealism", "Transcendental_idealism", "Philosophy_of_religion", "German"],
            "Influences": ["Immanuel_Kant", "Jean-Jacques_Rousseau", "Baruch_Spinoza"]
        },
        "Thomas_Hobbes": {
            "Era": "AD",
            "Year": 1679,
            "Attributes": ["Social_contract", "Political_philosophy"],
            "Influences": ["Aristotle", "René_Descartes", "Plato", "Cicero", "Niccolò_Machiavelli"]
        },
        "Cicero": {
            "Era": "BC",
            "Year": 43,
            "Attributes": ["Rhetoric", "Skepticism"],
            "Influences": ["Aristotle", "Socrates", "Plato"]
        },
        "Adam_Smith": {
            "Era": "AD",
            "Year": 1790,
            "Attributes": ["Economics", "Political_philosophy", "Liberalism"],
            "Influences": ["Aristotle", "John_Locke", "David_Hume"]
        },
        "Heraclitus": {
            "Era": "BC",
            "Year": 475,
            "Attributes": ["Pre_Socratic", "Ancient_Greek_philosophy"],
            "Influences": []
        },
        "Arthur_Schopenhauer": {
            "Era": "AD",
            "Year": 1860,
            "Attributes": ["German", "19th-century_philosophy", "Pessimism"],
            "Influences": ["Aristotle", "René_Descartes", "René_Descartes", "Voltaire", "David_Hume", "Jean-Jacques_Rousseau", "Immanuel_Kant", "Baruch_Spinoza", "John_Locke", "Plato"]
        },
        "Voltaire": {
            "Era": "AD",
            "Year": 1778,
            "Attributes": ["Liberalism", "Age_of_Enlightenment", "Political_philosophy", "French"],
            "Influences": ["Cicero", "Aristotle", "Plato", "Gottfried_Wilhelm_Leibniz", "John_Locke"]
        },
        "Niccolò_Machiavelli": {
            "Era": "AD",
            "Year": 1527,
            "Attributes": ["Republicanism", "Political_philosophy", "Realism"],
            "Influences": ["Cicero", "Aristotle", "Plato"]
        },
    }
