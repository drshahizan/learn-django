import { $$ } from "./utils.js";

function insertBrowserTiming() {
    console.log(["inserted"]);
    const timingOffset = performance.timing.navigationStart,
        timingEnd = performance.timing.loadEventEnd,
        totalTime = timingEnd - timingOffset;
    function getLeft(stat) {
        return ((performance.timing[stat] - timingOffset) / totalTime) * 100.0;
    }
    function getCSSWidth(stat, endStat) {
        let width =
            ((performance.timing[endStat] - performance.timing[stat]) /
                totalTime) *
            100.0;
        // Calculate relative percent (same as sql panel logic)
        width = (100.0 * width) / (100.0 - getLeft(stat));
        return width < 1 ? "2px" : width + "%";
    }
    function addRow(tbody, stat, endStat) {
        const row = document.createElement("tr");
        if (endStat) {
            // Render a start through end bar
            row.innerHTML =
                "<td>" +
                stat.replace("Start", "") +
                "</td>" +
                '<td><svg class="djDebugLineChart" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 100 5" preserveAspectRatio="none"><rect y="0" height="5" fill="#ccc" /></svg></td>' +
                "<td>" +
                (performance.timing[stat] - timingOffset) +
                " (+" +
                (performance.timing[endStat] - performance.timing[stat]) +
                ")</td>";
            row.querySelector("rect").setAttribute(
                "width",
                getCSSWidth(stat, endStat)
            );
        } else {
            // Render a point in time
            row.innerHTML =
                "<td>" +
                stat +
                "</td>" +
                '<td><svg class="djDebugLineChart" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 100 5" preserveAspectRatio="none"><rect y="0" height="5" fill="#ccc" /></svg></td>' +
                "<td>" +
                (performance.timing[stat] - timingOffset) +
                "</td>";
            row.querySelector("rect").setAttribute("width", 2);
        }
        row.querySelector("rect").setAttribute("x", getLeft(stat));
        tbody.appendChild(row);
    }

    const browserTiming = document.getElementById("djDebugBrowserTiming");
    // Determine if the browser timing section has already been rendered.
    if (browserTiming.classList.contains("djdt-hidden")) {
        const tbody = document.getElementById("djDebugBrowserTimingTableBody");
        // This is a reasonably complete and ordered set of timing periods (2 params) and events (1 param)
        addRow(tbody, "domainLookupStart", "domainLookupEnd");
        addRow(tbody, "connectStart", "connectEnd");
        addRow(tbody, "requestStart", "responseEnd"); // There is no requestEnd
        addRow(tbody, "responseStart", "responseEnd");
        addRow(tbody, "domLoading", "domComplete"); // Spans the events below
        addRow(tbody, "domInteractive");
        addRow(tbody, "domContentLoadedEventStart", "domContentLoadedEventEnd");
        addRow(tbody, "loadEventStart", "loadEventEnd");
        browserTiming.classList.remove("djdt-hidden");
    }
}

const djDebug = document.getElementById("djDebug");
// Insert the browser timing now since it's possible for this
// script to miss the initial panel load event.
insertBrowserTiming();
$$.onPanelRender(djDebug, "TimerPanel", insertBrowserTiming);
