

mybutton1 = CreateFrame("Button","mybutton",UIParent,"UIPanelButtonTemplate")
mybutton1:SetPoint("TOPLEFT", UIParent, "TOPLEFT", 50, -200)
mybutton1:SetWidth(100)
mybutton1:SetHeight(22)
mybutton1:SetText('0123456789')

xyzb = CreateFrame("Button","mybutton2",UIParent,"UIPanelButtonTemplate")
xyzb:SetPoint("TOPLEFT", UIParent, "TOPLEFT", 50, -120)
xyzb:SetWidth(150)
xyzb:SetHeight(22)
local xyzbcounter = 0
xyzb:SetScript("OnUpdate", function()
    xyzbcounter = xyzbcounter + 1
    countmod = math.mod(xyzbcounter, 5)
    if countmod == 1 then
        x, y = GetPlayerMapPosition("player")
        z = GetCurrentMapZone()
        x1 = string.format("%.f", x*10000)
        y1 = string.format("%.f", y*10000)
        xyid = z.."  |  "..x1.."  |  "..y1
        xyzb:SetText(xyid)
    end
end)


hp = CreateFrame("Button","mybutton2",UIParent,"UIPanelButtonTemplate")
hp:SetPoint("TOPLEFT", UIParent, "TOPLEFT", 205, -120)
hp:SetWidth(30)
hp:SetHeight(22)
local hpcounter = 0
hp:SetScript("OnUpdate", function()
    hpcounter = hpcounter + 1
    countmod = math.mod(hpcounter, 5)
    if countmod == 1 then
        f1 = UnitHealth("player")
        f2 = UnitHealthMax("player")
        f3 = 100 * (f1/f2)
        f = string.format("%.f", f3)
        if f == '100' then
            f = '99'
        end
        xyid = f
        hp:SetText(xyid)
    end
end)

local manacounter = 0
mana = CreateFrame("Button","mybutton2",UIParent,"UIPanelButtonTemplate")
mana:SetPoint("TOPLEFT", UIParent, "TOPLEFT", 240, -120)
mana:SetWidth(30)
mana:SetHeight(22)
local hpcounter = 0
mana:SetScript("OnUpdate", function()
    manacounter = manacounter + 1
    countmod = math.mod(manacounter, 5)
    if countmod == 1 then
        g1 = UnitMana("player")
        g2 = UnitManaMax("player")
        g3 = 100 * (g1/g2)
        g = string.format("%.f", g3)
        if g == '100' then
            g = '99'
        end
        xyid = g
        mana:SetText(xyid)
    end
end)

local counter = 0
newbutton = CreateFrame("Button","mybutton2",UIParent,"UIPanelButtonTemplate")
newbutton:SetPoint("TOPLEFT", UIParent, "TOPLEFT", 50, -150)
newbutton:SetWidth(100)
newbutton:SetHeight(22)
newbutton:SetScript("OnUpdate", function()
    counter = counter + 1
    countmod = math.mod(counter, 5)
    if countmod == 1 then
        z = GetMoney()
        xyid = z
        newbutton:SetText(xyid)
    end
end)