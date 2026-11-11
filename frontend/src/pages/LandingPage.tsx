import { ArrowRight, Bot, CandlestickChart, FileBarChart, ShieldCheck, Sparkles, Target } from 'lucide-react'
import { Link } from 'react-router-dom'
import { Logo } from '../components/ui/Logo'

const features = [
  {
    icon: Bot,
    title: 'Conversational AI assistant',
    text: 'Ask about any stock in plain language and get structured answers with sources and assumptions.',
  },
  {
    icon: CandlestickChart,
    title: 'Technical analysis',
    text: 'Candlestick charts with volume, RSI, MACD and moving averages across timeframes.',
  },
  {
    icon: FileBarChart,
    title: 'Fundamental analysis',
    text: 'Income statement, balance sheet, cash flow, valuation metrics and earnings history.',
  },
  {
    icon: Target,
    title: '5-year and 10-year goals',
    text: 'Set an investment goal and track your portfolio progress toward it.',
  },
  {
    icon: Sparkles,
    title: 'AI investment strategies',
    text: 'Explore long, short, diversification and balanced strategies with clearly labelled simulations.',
  },
  {
    icon: ShieldCheck,
    title: 'Transparent data',
    text: 'Every result shows its source, timestamp, reporting period and assumptions. Delayed data is labelled as delayed.',
  },
]

export function LandingPage() {
  return (
    <div className="min-h-screen bg-navy-900">
      <header className="mx-auto flex max-w-6xl items-center justify-between px-4 py-5 sm:px-6">
        <Logo className="text-lg" />
        <nav aria-label="Landing navigation" className="flex items-center gap-2">
          <Link
            to="/app/dashboard"
            className="rounded-lg px-3 py-2 text-sm font-medium text-ink-300 hover:bg-navy-700 hover:text-ink-100"
          >
            Dashboard
          </Link>
          <Link
            to="/app/assistant"
            className="rounded-lg bg-brand-600 px-3 py-2 text-sm font-medium text-white hover:bg-brand-500"
          >
            AI Assistant
          </Link>
        </nav>
      </header>

      <main>
        <section className="relative overflow-hidden">
          <div
            aria-hidden
            className="pointer-events-none absolute inset-x-0 -top-24 h-96 bg-[radial-gradient(ellipse_at_center,rgba(59,130,246,0.25),transparent_70%)]"
          />
          <div className="relative mx-auto max-w-4xl px-4 py-20 text-center sm:px-6 sm:py-28">
            <p className="mb-4 inline-block rounded-full border border-navy-600 bg-navy-800 px-3 py-1 text-xs font-medium text-brand-300">
              AI-powered stock market assistant
            </p>
            <h1 className="text-4xl font-bold tracking-tight text-ink-100 sm:text-6xl">
              Market data, research and analysis in one conversation
            </h1>
            <p className="mx-auto mt-6 max-w-2xl text-base text-ink-300 sm:text-lg">
              Financial Harness brings stock research, technical and fundamental analysis, portfolio tracking and
              AI-generated strategies together, so you can ask a question and see the evidence behind the answer.
            </p>
            <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
              <Link
                to="/app/assistant"
                className="inline-flex items-center gap-2 rounded-xl bg-brand-600 px-5 py-3 text-sm font-semibold text-white hover:bg-brand-500"
              >
                Ask the AI assistant <ArrowRight size={16} aria-hidden />
              </Link>
              <Link
                to="/app/dashboard"
                className="rounded-xl border border-navy-600 px-5 py-3 text-sm font-semibold text-ink-100 hover:bg-navy-800"
              >
                Open dashboard
              </Link>
            </div>
          </div>
        </section>

        <section aria-labelledby="features-heading" className="mx-auto max-w-6xl px-4 pb-24 sm:px-6">
          <h2 id="features-heading" className="mb-8 text-center text-2xl font-semibold text-ink-100">
            What you can do
          </h2>
          <ul className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {features.map(({ icon: Icon, title, text }) => (
              <li key={title} className="rounded-2xl border border-navy-600/60 bg-navy-800 p-5">
                <span className="mb-3 grid size-10 place-items-center rounded-lg bg-navy-700 text-brand-400" aria-hidden>
                  <Icon size={20} />
                </span>
                <h3 className="font-semibold text-ink-100">{title}</h3>
                <p className="mt-1 text-sm text-ink-300">{text}</p>
              </li>
            ))}
          </ul>
        </section>
      </main>

      <footer className="border-t border-navy-600/60 px-4 py-6 text-center text-xs text-ink-500">
        Financial Harness provides analysis for information only. It is not financial advice.
      </footer>
    </div>
  )
}
