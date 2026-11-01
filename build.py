# Edit SITE_NAME to rename the site, then run: python3 build.py
SITE_NAME="DSD Facts"
ML="https://medlineplus.gov/genetics/condition/"
S={
 "lee2006":("Lee PA, Houk CP, Ahmed SF, Hughes IA. Consensus statement on management of intersex disorders. Pediatrics. 2006;118(2):e488-500.","https://pubmed.ncbi.nlm.nih.gov/16882788/"),
 "lee2016":("Lee PA, et al. Global Disorders of Sex Development Update since 2006: Perceptions, Approach and Care. Horm Res Paediatr. 2016;85(3):158-80.","https://pubmed.ncbi.nlm.nih.gov/26820577/"),
 "blackless":("Blackless M, Charuvastra A, Derryck A, Fausto-Sterling A, Lauzanne K, Lee E. How sexually dimorphic are we? Review and synthesis. Am J Hum Biol. 2000;12(2):151-166.","https://doi.org/10.1002/(SICI)1520-6300(200003/04)12:2%3C151::AID-AJHB1%3E3.0.CO;2-F"),
 "sax":("Sax L. How common is intersex? A response to Anne Fausto-Sterling. J Sex Res. 2002;39(3):174-8.","https://pubmed.ncbi.nlm.nih.gov/12476264/"),
 "hull":("Hull CL. How sexually dimorphic are we? (commentary), with author reply by Fausto-Sterling. Am J Hum Biol. 2003;15(1):112-6.","https://pubmed.ncbi.nlm.nih.gov/12552585/"),
 "ks":("MedlinePlus Genetics: Klinefelter syndrome.",ML+"klinefelter-syndrome/"),
 "xxxy":("MedlinePlus Genetics: 48,XXXY syndrome.",ML+"48xxxy-syndrome/"),
 "xxxxy":("MedlinePlus Genetics: 49,XXXXY syndrome.",ML+"49xxxxy-syndrome/"),
 "ts":("MedlinePlus Genetics: Turner syndrome.",ML+"turner-syndrome/"),
 "ais":("MedlinePlus Genetics: Androgen insensitivity syndrome.",ML+"androgen-insensitivity-syndrome/"),
 "cah":("MedlinePlus Genetics: 21-hydroxylase deficiency.",ML+"21-hydroxylase-deficiency/"),
 "5ard":("MedlinePlus Genetics: 5-alpha reductase deficiency.",ML+"5-alpha-reductase-deficiency/"),
 "17b":("MedlinePlus Genetics: 17-beta hydroxysteroid dehydrogenase 3 deficiency.",ML+"17-beta-hydroxysteroid-dehydrogenase-3-deficiency/"),
 "swyer":("MedlinePlus Genetics: Swyer syndrome.",ML+"swyer-syndrome/"),
 "xxt":("MedlinePlus Genetics: 46,XX testicular difference of sex development.",ML+"46xx-testicular-difference-of-sex-development/"),
 "ency":("MedlinePlus Medical Encyclopedia: Differences of sex development.","https://medlineplus.gov/ency/article/001669.htm"),
 "mgd":("Corona LE, et al. Mixed Gonadal Dysgenesis: A Narrative Literature Review and Clinical Primer for the Urologist. J Urol. 2024.","https://pubmed.ncbi.nlm.nih.gov/38968141/"),
 "ovo":("Barros BA, et al. Are NR5A1 Variations a Frequent Cause of 46,XX Ovotesticular DSD? Single-center analysis and systematic review. Sex Dev. 2022.","https://pubmed.ncbi.nlm.nih.gov/36657429/"),
 "dsdf":("dsdfamilies (UK charity for families and young people with DSD).","https://www.dsdfamilies.org/"),
 "aissg":("AIS-DSD Support Group / AISSG.","https://www.aissg.org/"),
 "cares":("CARES Foundation (congenital adrenal hyperplasia).","https://caresfoundation.org/"),
}
keys=list(S)
def c(k): return f'<sup><a href="sources.html#{k}">[{keys.index(k)+1}]</a></sup>'
NAV=[("index.html","Home"),("conditions.html","Conditions"),("myths.html","Myths vs Facts"),("voices.html","Voices &amp; Resources"),("sources.html","Sources"),("about.html","About")]
def page(fn,title,body):
    nav="".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==fn else ""}>{t}</a></li>' for h,t in NAV)
    open(fn,"w").write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {SITE_NAME}</title><meta name="description" content="Evidence-based information about differences of sex development (DSD).">
<link rel="stylesheet" href="style.css"></head><body><a class="skip" href="#main">Skip to content</a>
<header><div class="wrap"><a class="brand" href="index.html">{SITE_NAME}</a><nav aria-label="Main"><ul>{nav}</ul></nav></div></header>
<main id="main" class="wrap">{body}</main>
<footer><div class="wrap"><p>{SITE_NAME} is an educational resource, not medical advice. See <a href="about.html">About &amp; disclaimer</a>. Draft, last reviewed Oct 2026.</p></div></footer></body></html>''')

page("index.html","Home",f'''<section class="hero"><h1>Accurate information about differences of sex development</h1>
<p class="lead">Differences (or disorders) of sex development, called DSDs and often referred to as intersex conditions, are congenital conditions in which chromosomal, gonadal, or anatomical sex develops atypically.{c("lee2006")} Each one is a specific medical diagnosis with its own causes, care needs, and lived experience.</p>
<p><a class="btn" href="conditions.html">Explore conditions</a> <a class="btn alt" href="myths.html">Myths vs facts</a></p></section>
<h2>Our mission</h2><ul>
<li><strong>Get the facts right.</strong> Every claim here links to a medical or peer-reviewed source.</li>
<li><strong>Correct misinformation calmly.</strong> We correct inaccurate claims with evidence. We don't attack people.</li>
<li><strong>Center people with DSDs.</strong> These conditions belong first to the people and families who live with them. Their health needs, privacy, and voices come first.</li></ul>
<div class="cards">
<a class="card" href="conditions.html"><h3>Conditions</h3><p>Karyotype, biology, presentation, prevalence, and health needs for 11 conditions.</p></a>
<a class="card" href="myths.html"><h3>Myths vs facts</h3><p>"Two full sets of genitals," the 1.7% figure, what XXY means, and more.</p></a>
<a class="card" href="voices.html"><h3>Voices &amp; resources</h3><p>Patient-led organizations and support groups.</p></a></div>''')

C=[
("Klinefelter syndrome","47,XXY",f"An extra X chromosome in people with a Y chromosome. The testes are small and produce less testosterone.{c('ks')}","Male development. Often diagnosed at puberty or during infertility evaluation: small testes, reduced testosterone, possible breast development, taller stature, and learning or language differences in some people.{c}".replace("{c}",c('ks')),f"About 1 in 650 male newborns. It is the most common sex chromosome disorder.{c('ks')}","Testosterone therapy, fertility counselling, and educational support. Many people are never diagnosed."),
("48,XXXY and 49,XXXXY","48,XXXY / 49,XXXXY",f"Two or three extra X chromosomes alongside a Y. Effects are generally more pronounced than in 47,XXY.{c('xxxy')}{c('xxxxy')}","Boys and men with small testes and low testosterone. Developmental, speech, and learning differences are common, and 49,XXXXY often involves skeletal and heart differences.","48,XXXY: 1 in 17,000 to 1 in 50,000 newborn boys."+c('xxxy')+" 49,XXXXY: about 1 in 85,000 to 100,000 babies born with a Y chromosome."+c('xxxxy'),"Hormone therapy, developmental therapies, and multidisciplinary care."),
("Turner syndrome","45,X (also mosaic forms)",f"Complete or partial loss of one X chromosome.{c('ts')}","Female development, short stature, and ovarian insufficiency (usually no spontaneous puberty). Some people have heart or kidney differences.","About 1 in 2,000 female newborns, and much more common among miscarriages."+c('ts'),"Growth hormone, estrogen replacement, cardiac monitoring, and fertility counselling."),
("Complete androgen insensitivity (CAIS)","46,XY",f"Variants in the <em>AR</em> gene mean the body's cells cannot respond to androgens (testosterone). Testes form and make testosterone, but the body develops along female lines.{c('ais')}","Typical female external anatomy. There is no uterus, and the testes are internal. Often diagnosed when periods don't start, or when an inguinal hernia is found in childhood.","2 to 5 in 100,000 newborn females."+c('ais'),"Decisions about gonad removal and its timing, hormone replacement if the gonads are removed, bone health, and psychological support."),
("Partial androgen insensitivity (PAIS)","46,XY",f"Partial response to androgens because of <em>AR</em> variants.{c('ais')}","Wide range of genital appearance, from mostly female to mostly male, including atypical genitalia.","Thought to be at least as common as CAIS."+c('ais'),"Individualized care. Sex of rearing and any surgery are among the most debated questions (see <a href=\"myths.html#debated\">debated questions</a>)."),
("Congenital adrenal hyperplasia (CAH, 21-hydroxylase deficiency)","Usually 46,XX or 46,XY",f"An enzyme deficiency reduces cortisol (and often aldosterone) production, and the adrenal glands overproduce androgens.{c('cah')}","Classic salt-wasting CAH can be life-threatening in newborns. 46,XX infants may have atypical genitalia but have ovaries and a uterus. Non-classic forms appear later.","Classic: about 1 in 15,000 newborns. Non-classic: about 1 in 1,000."+c('cah'),"Lifelong steroid replacement, adrenal crisis prevention, and newborn screening. Support: CARES Foundation."+c('cares')),
("5-alpha-reductase deficiency","46,XY",f"<em>SRD5A2</em> variants reduce conversion of testosterone to DHT, which is needed for typical male external genital development before birth.{c('5ard')}","At birth the genitals may look female or atypical. Masculinization often occurs at puberty, and some people raised as girls change to a male gender role.","Rare, and exact incidence unknown. Clusters have been found in the Dominican Republic, Papua New Guinea, Turkey, and Egypt."+c('5ard'),"Specialist assessment, informed choices about sex of rearing, and fertility support."),
("17β-HSD3 deficiency","46,XY",f"<em>HSD17B3</em> variants impair testosterone production in the testes.{c('17b')}","Often female-appearing at birth, with virilization at puberty.","About 1 in 147,000 newborns, and higher in some populations (1 in 200 to 300 in the Arab population of Gaza)."+c('17b'),"Similar to 5-ARD: specialist care and shared decision-making."),
("Ovotesticular DSD","46,XX most often; also 46,XY or mosaic",f"Both ovarian and testicular tissue are present, either in one gonad (an ovotestis) or as one ovary and one testis.{c('ency')}","External genitalia may be ambiguous, or may look female or male. The cause is usually unknown.{c('ency')}","Rare. We could not verify a reliable population prevalence from an authoritative source. Genetic causes are under study.{c('ovo')}","Gonadal assessment, tumor surveillance, and individualized care."),
("Mixed gonadal dysgenesis","Usually 45,X/46,XY mosaic",f"Asymmetric gonads, typically a testis on one side and an underdeveloped 'streak' gonad on the other.{c('mgd')}","Broad range, from female-appearing to male-appearing genitals. Some people have features of Turner syndrome.","Rare. Prevalence figure not verified for this draft.{c('mgd')}","Gonadal tumor risk monitoring, growth, hormone, and fertility care."),
("Swyer syndrome (46,XY complete gonadal dysgenesis)","46,XY",f"The gonads do not develop into testes (they remain 'streak' gonads). About 15% of cases involve <em>SRY</em> variants.{c('swyer')}","Female anatomy with a uterus. Puberty does not start without treatment.","About 1 in 80,000 people."+c('swyer'),"Estrogen/progesterone therapy, removal of streak gonads because of high tumor risk, and pregnancy via donor eggs is possible."),
("46,XX testicular DSD","46,XX",f"Testes develop despite an XX karyotype, most often because the <em>SRY</em> gene has moved onto an X chromosome.{c('xxt')}","Usually male appearance. Small testes, infertility, and sometimes atypical genitalia.","About 1 in 20,000 individuals with a male appearance."+c('xxt'),"Testosterone therapy and fertility counselling."),
]
rows="".join(f'''<article class="cond" id="c{i}"><h2>{n}</h2><dl><dt>Karyotype</dt><dd>{k}</dd><dt>Biology</dt><dd>{b}</dd><dt>Typical presentation</dt><dd>{p}</dd><dt>Prevalence</dt><dd>{pr}</dd><dt>Health needs</dt><dd>{h}</dd></dl></article>''' for i,(n,k,b,p,pr,h) in enumerate(C))
toc="".join(f'<li><a href="#c{i}">{x[0]}</a></li>' for i,x in enumerate(C))
page("conditions.html","Conditions",f'''<h1>Conditions</h1><p class="lead">The 2006 Consensus Statement grouped DSDs into sex chromosome DSD, 46,XY DSD, and 46,XX DSD.{c("lee2006")} Each condition below is distinct. Grouping them under one label can hide very different needs.</p><nav class="toc" aria-label="Conditions"><ul>{toc}</ul></nav>{rows}''')

page("myths.html","Myths vs Facts",f'''<h1>Myths vs facts</h1><p class="lead">These are common claims, with what the medical evidence says.</p>
<article class="myth"><h2>Myth: Intersex people have "two full sets of genitals."</h2><p><strong>Fact:</strong> No DSD produces two complete, functioning sets of external genitals. The closest condition is <a href="conditions.html#c8">ovotesticular DSD</a>, which involves <em>gonadal tissue</em> (ovarian and testicular), either in one ovotestis or as one ovary and one testis. External genitals may be ambiguous, or may look typically female or male.{c("ency")}</p></article>
<article class="myth"><h2>Myth: "1.7% of people are intersex."</h2><p><strong>Fact:</strong> The 1.7% figure comes from Blackless, Fausto-Sterling and colleagues (2000).{c("blackless")} It counts a broad set of conditions, including Klinefelter syndrome, Turner syndrome, and late-onset (non-classic) CAH. Sax (2002) argued that most clinicians don't classify these as intersex. Restricting the term to cases where chromosomal sex is inconsistent with phenotypic sex, or the phenotype is not classifiable as male or female, gives about <strong>0.018%</strong>, "almost 100 times lower."{c("sax")} The difference comes mostly from <em>definitions</em>, so any prevalence figure should state which conditions it includes. Fausto-Sterling's reply to critics is also published.{c("hull")}</p></article>
<article class="myth"><h2>Myth: XXY means a person is "both sexes."</h2><p><strong>Fact:</strong> 47,XXY (Klinefelter syndrome) is a sex chromosome variation in people with a Y chromosome, who develop testes and male anatomy. The main effects are lower testosterone and infertility.{c("ks")} Most clinicians do not consider it intersex in the sense of ambiguous anatomy.{c("sax")} The same applies to 48,XXXY and 49,XXXXY, which affect boys and men.{c("xxxy")}{c("xxxxy")}</p></article>
<article class="myth"><h2>Myth: "Androgen sensitivity" makes someone male and female.</h2><p><strong>Fact:</strong> The condition is androgen <em>in</em>sensitivity. Because of <em>AR</em> gene variants, the body's cells can't respond (fully or partly) to testosterone. In the complete form, people with 46,XY chromosomes and internal testes develop typical female external anatomy and usually live as women.{c("ais")}</p></article>
<section id="debated"><h2>Genuinely debated questions</h2>
<article class="myth"><h3>"Intersex" vs "DSD" terminology</h3><p>The 2006 Consensus introduced "disorders of sex development" to replace terms like "hermaphrodite" and "pseudohermaphrodite."{c("lee2006")} The 2016 update reports continued disagreement: some patients and advocates find "disorder" stigmatizing and prefer "differences" or "intersex," while others prefer a specific diagnosis over any umbrella term.{c("lee2016")} This site uses "DSD" and the condition name, and respects each person's preferred language.</p></article>
<article class="myth"><h3>Timing of genital surgery</h3><p>The 2006 Consensus called for care by multidisciplinary teams, open communication, and caution about surgery.{c("lee2006")} The 2016 global update notes there is still not enough outcome evidence on early versus deferred surgery, and that views differ among clinicians, parents, and adults with DSD.{c("lee2016")} We present this as an open question.</p></article>
<article class="myth"><h3>Which conditions count as intersex?</h3><p>Broad definitions (Blackless et al.){c("blackless")} and narrow ones (Sax){c("sax")} both have published defenders. We list what each definition includes rather than choosing one figure.</p></article></section>''')

page("voices.html","Voices & Resources",f'''<h1>Voices &amp; resources</h1><p class="lead">The best sources on living with a DSD are the people and families themselves. These organizations are run by or with them.</p>
<div class="cards">
<a class="card" href="{S['dsdf'][1]}"><h3>dsdfamilies</h3><p>UK charity offering information and support for families, children, and young people with DSD.</p></a>
<a class="card" href="{S['aissg'][1]}"><h3>AIS-DSD Support Group</h3><p>Peer support for people with androgen insensitivity and related conditions.</p></a>
<a class="card" href="{S['cares'][1]}"><h3>CARES Foundation</h3><p>Support and education for congenital adrenal hyperplasia.</p></a>
<a class="card" href="https://medlineplus.gov/"><h3>MedlinePlus (NIH)</h3><p>Plain-language medical and genetics information.</p></a></div>
<h2>Personal stories</h2><p><em>Placeholder.</em> Personal stories will be added only from published, attributable sources, quoted word for word and linked, or with written permission from contributors.</p>''')

li="".join(f'<li id="{k}">{t} <a href="{u}">{u}</a></li>' for k,(t,u) in S.items())
page("sources.html","Sources",f'<h1>Sources</h1><p>Numbers match the citations throughout the site. All links were checked in October 2026.</p><ol class="bib">{li}</ol>')

page("about.html","About",f'''<h1>About {SITE_NAME}</h1><p>{SITE_NAME} is an independent educational project. Its goal is to provide accurate, sourced information about differences of sex development, to correct misinformation respectfully, and to keep the focus on people who live with these conditions.</p>
<h2>Editorial standards</h2><ul><li>Every factual claim cites a medical body, peer-reviewed publication, or established patient organization.</li><li>We correct claims, not people.</li><li>Where experts disagree, we present each side with sources.</li><li>Corrections are welcome and will be dated.</li></ul>
<h2 id="disclaimer">Medical disclaimer</h2><p class="note">This site is for general education only and is <strong>not medical advice</strong>. It doesn't replace diagnosis or treatment by qualified clinicians. If you or your child may have a DSD, talk to a specialist team (endocrinology, urology/gynecology, genetics, and psychology). In an emergency, such as signs of adrenal crisis in CAH, seek urgent care immediately.</p>''')
