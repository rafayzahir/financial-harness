import { Bot } from 'lucide-react'
import { Link } from 'react-router-dom'
import { Card } from '../components/ui/Card'
import { PageHeader } from '../components/ui/PageHeader'
import { ApiPendingState } from '../components/ui/StateViews'
import { isApiConfigured } from '../config/env'

/**
 * Dashboard shell. Every card is empty until its real API exists.
 * No sample numbers are shown on purpose.
 */
export function DashboardPage() {
  return (
    <>
      <PageHeader
        title="Dashboard"
        description="Your portfolio, the market and your goals in one place."
        action={
          <Link
            to="/app/assistant"
            className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-4 py-2 text-sm font-medium text-white hover:bg-brand-500"
          >
            <Bot size={16} aria-hidden /> Ask the AI assistant
          </Link>
        }
      />

      {!isApiConfigured && (
        <p role="status" className="mb-6 rounded-xl border border-warn/40 bg-warn/10 px-4 py-3 text-sm text-warn">
          Backend URL is not set yet. Add VITE_API_BASE_URL in your .env file once Danial shares it.
        </p>
      )}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
        <Card title="Total portfolio value" className="xl:col-span-1">
          <ApiPendingState dependency="Danial: portfolio API" />
        </Card>
        <Card title="Asset allocation">
          <ApiPendingState dependency="Danial: portfolio API" />
        </Card>
        <Card title="Risk information">
          <ApiPendingState dependency="Danial: risk API" />
        </Card>
        <Card title="Stock performance" className="md:col-span-2">
          <ApiPendingState dependency="Danial: portfolio and market data APIs" />
        </Card>
        <Card title="Market overview">
          <ApiPendingState dependency="Danial: market data API" />
        </Card>
        <Card title="Financial goal progress">
          <ApiPendingState dependency="Danial: financial goals API" />
        </Card>
        <Card title="Recent analyses" className="md:col-span-2">
          <ApiPendingState dependency="Danial: saved analysis results API" />
        </Card>
      </div>
    </>
  )
}
