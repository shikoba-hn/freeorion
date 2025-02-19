from common.base_prod import TECH_COST_MULTIPLIER

Tech(
    name="GRO_MEGA_ECO",
    description="GRO_MEGA_ECO_DESC",
    short_description="GRO_MEGA_ECO_SHORT_DESC",
    category="GROWTH_CATEGORY",
    researchcost=135 * TECH_COST_MULTIPLIER,
    researchturns=9,
    tags=["PEDIA_GROWTH_CATEGORY"],
    prerequisites=[
        "SHP_ENDOCRINE_SYSTEMS",
        "GRO_TERRAFORM",
        "GRO_NANOTECH_MED",
    ],
    unlock=Item(type=Building, name="BLD_NEST_ERADICATOR"),
    graphic="icons/tech/megafauna_ecology.png",
)
