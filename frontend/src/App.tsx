import { Navigate, Route, Routes } from 'react-router-dom'
import { AppLayout } from './layouts/AppLayout'
import { AssistantPage } from './pages/AssistantPage'
import { DashboardPage } from './pages/DashboardPage'
import { LandingPage } from './pages/LandingPage'
import { ModulePage } from './pages/ModulePage'
import { navItems } from './routes/navigation'

// Pages that already have their own screen. The rest use the temporary ModulePage shell.
const customPages: Record<string, React.ReactElement> = {
  dashboard: <DashboardPage />,
  assistant: <AssistantPage />,
}

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/app" element={<AppLayout />}>
        <Route index element={<Navigate to="dashboard" replace />} />
        {navItems.map((item) => (
          <Route key={item.path} path={item.path} element={customPages[item.path] ?? <ModulePage item={item} />} />
        ))}
      </Route>
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
