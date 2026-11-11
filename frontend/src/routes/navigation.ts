import {
  Bot,
  BriefcaseBusiness,
  CandlestickChart,
  FileBarChart,
  GitCompareArrows,
  History,
  LayoutDashboard,
  ListChecks,
  Search,
  Sparkles,
  Target,
} from 'lucide-react'
import type { LucideIcon } from 'lucide-react'

export interface NavItem {
  path: string
  label: string
  icon: LucideIcon
  description: string
  /** What must exist before this page can show real data (shown in the UI) */
  dependency: string
}

export const navItems: NavItem[] = [
  {
    path: 'dashboard',
    label: 'Dashboard',
    icon: LayoutDashboard,
    description: 'Portfolio overview, market overview, goals and recent analyses.',
    dependency: 'Danial: portfolio, market overview, goals and saved-analyses APIs',
  },
  {
    path: 'assistant',
    label: 'AI Assistant',
    icon: Bot,
    description: 'Ask stock market questions in plain language.',
    dependency: 'Danial: chat API. Hamid: AI response JSON structure',
  },
  {
    path: 'search',
    label: 'Stock Search',
    icon: Search,
    description: 'Search companies by name or ticker and open company research.',
    dependency: 'Danial: stock search and company information APIs',
  },
  {
    path: 'technical',
    label: 'Technical Analysis',
    icon: CandlestickChart,
    description: 'Candlestick charts, volume, RSI, MACD and moving averages.',
    dependency: 'Danial: technical analysis data API (OHLC, volume, indicators)',
  },
  {
    path: 'fundamental',
    label: 'Fundamental Analysis',
    icon: FileBarChart,
    description: 'Income statement, balance sheet, cash flow, valuation and earnings history.',
    dependency: 'Danial: fundamental analysis data API',
  },
  {
    path: 'compare',
    label: 'Compare Stocks',
    icon: GitCompareArrows,
    description: 'Compare prices, performance, metrics and indicators side by side.',
    dependency: 'Danial: stock comparison API. Hamid: comparison summary',
  },
  {
    path: 'portfolio',
    label: 'Portfolio',
    icon: BriefcaseBusiness,
    description: 'Manage holdings, view allocation, analytics and risk.',
    dependency: 'Danial: portfolio and risk APIs',
  },
  {
    path: 'goals',
    label: 'Financial Goals',
    icon: Target,
    description: 'Create and track 5-year and 10-year investment goals.',
    dependency: 'Danial: financial goals API',
  },
  {
    path: 'strategies',
    label: 'AI Strategies',
    icon: Sparkles,
    description: 'Long, short, diversification and balanced strategies with simulations.',
    dependency: 'Hamid: strategy and simulation JSON. Danial: strategy results API',
  },
  {
    path: 'tasks',
    label: 'Analysis Progress',
    icon: ListChecks,
    description: 'Follow background analyses: queued, running, completed or failed.',
    dependency: 'Danial: Celery task submission and status APIs',
  },
  {
    path: 'saved',
    label: 'Saved Analyses',
    icon: History,
    description: 'Open previously completed analyses with sources and assumptions.',
    dependency: 'Danial: saved analysis results API',
  },
]
