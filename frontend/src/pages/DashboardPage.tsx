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
        eyebrow="Overview"
        title="Dashboard"
        description="Your portfolio, the market and your goals in one place."
        action={
          <Link to="/app/assistant" className="btn btn-primary">
            <Bot size={16} aria-hidden /> Ask the AI assistant
          </Link>
        }
      />

      {!isApiConfigured && (
        <p
          role="status"
          className="enter mb-6 rounded border border-caution/30 bg-caution/10 px-4 py-3 text-sm text-caution-light"
          style={{ '--d': '60ms' } as React.CSSProperties}
        >
          Backend URL is not set yet. Add <span className="num">VITE_API_BASE_URL</span> in your .env file once Danial shares it.
        </p>
      )}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-12">
        <Card title="Total portfolio value" delay={80} className="xl:col-span-4">
          <ApiPendingState dependency="Danial: portfolio API" />
        </Card>
        <Card title="Asset allocation" delay={140} className="xl:col-span-4">
          <ApiPendingState dependency="Danial: portfolio API" />
        </Card>
        <Card title="Risk information" delay={200} className="md:col-span-2 xl:col-span-4">
          <ApiPendingState dependency="Danial: risk API" />
        </Card>
        <Card title="Stock performance" delay={260} className="md:col-span-2 xl:col-span-8">
          <ApiPendingState dependency="Danial: portfolio and market data APIs" />
        </Card>
        <Card title="Market overview" delay={320} className="md:col-span-2 xl:col-span-4">
          <ApiPendingState dependency="Danial: market data API" />
        </Card>
        <Card title="Financial goal progress" delay={380} className="xl:col-span-4">
          <ApiPendingState dependency="Danial: financial goals API" />
        </Card>
        <Card title="Recent analyses" delay={440} className="md:col-span-2 xl:col-span-8">
          <ApiPendingState dependency="Danial: saved analysis results API" />
        </Card>
      </div>
    </>
  )
}
