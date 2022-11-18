local myFrame
local myFontString
local myName



local backdropInfo = {
    bgFile		= "Interface/Tooltips/UI-Tooltip-Background",
    edgeFile	= "Interface/Tooltips/UI-Tooltip-Border",
    tile 		= true,
    tileEdge	= true,
    edgeSize = 16,
    insets = { left = 4, right = 4, top = 4, bottom = 4 },
}

mybutton1 = CreateFrame("Button","mybutton",UIParent,"UIPanelButtonTemplate")
mybutton1:SetPoint("TOPLEFT", UIParent, "TOPLEFT", 100, -280)
mybutton1:SetWidth(100)
mybutton1:SetHeight(22)
mybutton1:SetText('0123456789')

mybutton = CreateFrame("Button","mybutton2",UIParent,"UIPanelButtonTemplate")
mybutton:SetPoint("TOPLEFT", UIParent, "TOPLEFT", 100, -120)
mybutton:SetWidth(250)
mybutton:SetHeight(22)
x, y = GetPlayerMapPosition("player")
x1 = string.format("%.2f", x*10000)
y1 = string.format("%.2f", x*10000)
xyid = "x:"..x..",y:"..y
mybutton:SetText("哈哈")
br = true
mybutton:SetScript("OnClick", function (self, button, down)
    local j,k=UnitName("player");
    x, y = GetPlayerMapPosition("player")
    x1 = string.format("%.2f", x*10000)
    y1 = string.format("%.2f", y*10000)
    xyid = x1.."|"..y1
    mybutton:SetText(xyid)
end);
mybutton:RegisterEvent("PLAYER_STARTED_MOVING")
mybutton:RegisterEvent("PLAYER_STOPPED_MOVING")
mybutton:RegisterEvent("UNIT_COMBAT")
local counter = 0
mybutton:SetScript("OnUpdate", function()
    counter = counter + 1
    --countmod = math.random(5)
    countmod = math.mod(counter, 5)
    if countmod == 1 then
        x, y = GetPlayerMapPosition("player")
        z = GetCurrentMapZone()
        x1 = string.format("%.f", x*10000)
        y1 = string.format("%.f", y*10000)
        f = UnitHealth("player")
        f1 = string.format("%.f", f)
        g = UnitMana("player")
        f2 = string.format("%.f", g)
        xyid = z.."  |  "..x1.."  |  "..y1 .."  |  "..f1.."  |  "..f2
        mybutton:SetText(xyid)
    end
end)

newbutton = CreateFrame("Button","mybutton2",UIParent,"UIPanelButtonTemplate")
newbutton:SetPoint("TOPLEFT", UIParent, "TOPLEFT", 100, -150)
newbutton:SetWidth(250)
newbutton:SetHeight(22)
newbutton:SetScript("OnUpdate", function()
    counter = counter + 1
    --countmod = math.random(5)
    countmod = math.mod(counter, 5)
    if countmod == 1 then
        z = GetMoney()
        xyid = z
        newbutton:SetText(xyid)
    end
end)