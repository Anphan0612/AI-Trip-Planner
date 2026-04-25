# PLAN: Frontend AI Itinerary Generation

## Overview
This plan outlines the steps to connect the React frontend to the AI service (via the Spring Boot backend) to generate and display a trip itinerary.

## Project Type
WEB (React/TypeScript Frontend)

## Success Criteria
- User can trigger itinerary generation from the frontend UI.
- Application handles long-polling or loading state gracefully (up to 60s timeout).
- Generated itinerary data is successfully fetched and rendered in the UI without errors.

## Tech Stack
- **Frontend**: React, TypeScript, Axios (configured in `api.ts`)
- **Backend API**: Spring Boot (`TripController`)
- **AI Service**: FastAPI (`ai_service`)

## Open Questions (Socratic Gate)
> [!IMPORTANT] 
> **User Review Required before Implementation:**
> 1. **Flow Trigger**: Where exactly in the UI should this generation be triggered? (e.g., automatically after a form submission, or via a specific "Generate AI Itinerary" button on a trip details page?) => Button: "
> 2. **State Management**: Should we use React Context, Redux, or simple local state + React Query to manage the loading state and fetched itinerary data?
> 3. **Direct vs Gateway**: The current `api.ts` routes requests through the Spring Boot backend (`tripApi.generate`). Are we sticking to this architecture, or do you want the frontend to call the FastAPI `ai_service` directly?

## File Structure (Relevant files)
```text
FluidConcierge/src/
├── services/
│   └── api.ts (already contains tripApi.generate)
├── components/
│   ├── explore/
│   │   └── TripGeneratorUI.tsx (TBD)
│   └── layout/
├── pages/
│   └── TripDetailsPage.tsx (TBD)
```

## Task Breakdown

| Task ID | Name | Agent | Skills | Priority | Dependencies | INPUT → OUTPUT → VERIFY |
|---------|------|-------|--------|----------|--------------|-------------------------|
| 1 | **Create Loading Component** | `frontend-specialist` | `frontend-design` | P1 | None | **IN**: Text prop <br>**OUT**: Skeleton/Spinner UI <br>**VERIFY**: Renders correctly during long AI wait times |
| 2 | **Implement Generation Hook** | `frontend-specialist` | `react-best-practices` | P1 | None | **IN**: Trip ID <br>**OUT**: `useGenerateItinerary` hook handling loading/error <br>**VERIFY**: Hook calls `tripApi.generate` and updates state |
| 3 | **Build Generate Button/Trigger** | `frontend-specialist` | `frontend-design` | P2 | Task 2 | **IN**: Hook state <br>**OUT**: Interactive button <br>**VERIFY**: Button is disabled while loading, triggers hook on click |
| 4 | **Render Itinerary View** | `frontend-specialist` | `frontend-design` | P2 | Task 2 | **IN**: `GenerateResponse` data <br>**OUT**: Daily schedule UI <br>**VERIFY**: Activities are grouped by day and displayed correctly |

## Phase X: Verification
- [ ] No purple/violet hex codes used in new UI components.
- [ ] No standard generic template layouts used.
- [ ] Socratic Gate questions answered by user.
- [ ] `npm run lint && npx tsc --noEmit` passes on frontend.
- [ ] UX Audit (`ux_audit.py`) passes for the new generation flow.
